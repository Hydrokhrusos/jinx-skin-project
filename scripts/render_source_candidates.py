import argparse
import hashlib
import json
import os
import sys
import tempfile

import bpy
from mathutils import Vector


HIDDEN_MATERIAL_TOKENS = (
    "recall",
    "emote",
    "photo",
    "jelly",
    "babywolf",
    "slotmachine",
    "flag",
    "torch",
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--champion", default="jinx")
    parser.add_argument("--skins", required=True)
    parser.add_argument("--addon-root", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--report", required=True)
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else sys.argv[1:]
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def look_at(obj, target):
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()


def load_tex_image(path, tex_to_dds_bytes):
    descriptor, temporary = tempfile.mkstemp(suffix=".dds")
    os.close(descriptor)
    try:
        with open(temporary, "wb") as handle:
            handle.write(tex_to_dds_bytes(os.path.abspath(path)))
        image = bpy.data.images.load(temporary, check_existing=False)
        image.name = os.path.basename(path)
        image.pack()
        image.colorspace_settings.name = "sRGB"
        return image
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)


def configure_material(material, image, hidden=False):
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    if hidden:
        shader.inputs["Alpha"].default_value = 0.0
        material.surface_render_method = "DITHERED"
    else:
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        texture.interpolation = "Linear"
        shader.inputs["Roughness"].default_value = 0.72
        shader.inputs["Specular IOR Level"].default_value = 0.28
        links.new(texture.outputs["Color"], shader.inputs["Base Color"])
        links.new(texture.outputs["Alpha"], shader.inputs["Alpha"])
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])


def texture_priority(path, role):
    name = os.path.basename(path).lower()
    score = 0
    if role == "weapon" and "weapon" in name:
        score += 100
    if role == "hair" and "hair" in name:
        score += 100
    if role == "body" and "main_tx_cm" in name:
        score += 90
    if role == "body" and name.endswith("_tx_cm.tex"):
        score += 70
    if role == "body" and "body" in name:
        score += 40
    if "mask" in name or "recall" in name or "emote" in name or "gradient" in name:
        score -= 100
    return score


def choose_image(material_name, paths, images):
    lowered = material_name.lower()
    if "weapon" in lowered or "gun" in lowered:
        role = "weapon"
    elif "hair" in lowered or "hood" in lowered:
        role = "hair"
    else:
        role = "body"
    selected = max(paths, key=lambda path: texture_priority(path, role))
    return images[selected]


def reset_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.armatures, bpy.data.materials, bpy.data.images):
        for datablock in list(datablocks):
            if datablock.users == 0:
                datablocks.remove(datablock)


def add_area(name, location, energy, size, color, target):
    data = bpy.data.lights.new(name, "AREA")
    data.energy = energy
    data.shape = "DISK"
    data.size = size
    data.color = color
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    look_at(obj, target)


def render_skin(args, skin, import_skl, import_skn, tex_to_dds_bytes):
    reset_scene()
    champion = args.champion.lower()
    folder = os.path.abspath(os.path.join(args.root, f"assets/characters/{champion}/skins/skin{skin}"))
    stem = os.path.join(folder, f"{champion}_skin{skin}")
    joints, influences = import_skl.read_skl(stem + ".skl")
    armature = import_skl.create_armature(joints, bone_orient="VISUAL")
    indices, vertices, submeshes = import_skn.read_skn(stem + ".skn")
    mesh = import_skn.create_mesh(
        indices,
        vertices,
        submeshes,
        f"{args.champion.title()}_Skin{skin}_Candidate",
        armature,
        joints,
        influences,
    )
    armature.hide_render = True

    texture_paths = [
        os.path.join(folder, name)
        for name in os.listdir(folder)
        if name.lower().endswith(".tex")
    ]
    if not texture_paths:
        raise ValueError(f"No root textures found for skin {skin}")
    images = {path: load_tex_image(path, tex_to_dds_bytes) for path in texture_paths}
    hidden_materials = set()
    for material in mesh.data.materials:
        hidden = any(token in material.name.lower() for token in HIDDEN_MATERIAL_TOKENS)
        if hidden:
            hidden_materials.add(material.name.lower())
        configure_material(material, choose_image(material.name, texture_paths, images), hidden=hidden)

    visible_vertex_indices = set()
    for polygon in mesh.data.polygons:
        material_name = mesh.data.materials[polygon.material_index].name.lower()
        if material_name not in hidden_materials:
            visible_vertex_indices.update(polygon.vertices)
    world_points = [mesh.matrix_world @ mesh.data.vertices[index].co for index in visible_vertex_indices]
    minimum = Vector(tuple(min(point[i] for point in world_points) for i in range(3)))
    maximum = Vector(tuple(max(point[i] for point in world_points) for i in range(3)))
    target = (minimum + maximum) * 0.5
    extent = maximum - minimum
    distance = max(extent) * 2.5

    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 640
    scene.render.resolution_y = 640
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.world.color = (0.018, 0.022, 0.032)

    camera_data = bpy.data.cameras.new("Candidate_Camera")
    camera = bpy.data.objects.new("Candidate_Camera", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    camera_data.type = "ORTHO"

    add_area("Key", target + Vector((-2.8, -3.4, 3.4)), 1050, 4.0, (0.9, 0.95, 1.0), target)
    add_area("Rim", target + Vector((3.0, 2.2, 2.8)), 900, 3.5, (0.35, 0.65, 1.0), target)
    add_area("Fill", target + Vector((2.0, -2.0, 0.8)), 500, 3.0, (0.75, 0.55, 1.0), target)

    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)
    views = {
        "front": target + Vector((0.0, -distance, 0.1 * extent.z)),
        "side": target + Vector((distance, 0.0, 0.1 * extent.z)),
        "back": target + Vector((0.0, distance, 0.1 * extent.z)),
    }
    outputs = []
    for name, location in views.items():
        camera_data.ortho_scale = max(extent.z * 1.15, (extent.x if name != "side" else extent.y) * 1.35)
        camera.location = location
        look_at(camera, target)
        output = os.path.join(out_dir, f"skin{skin}_{name}.png")
        scene.render.filepath = output
        bpy.ops.render.render(write_still=True)
        outputs.append({"view": name, "path": output, "sha256": sha256_file(output)})

    return {
        "champion": args.champion,
        "skin": skin,
        "model": stem + ".skn",
        "vertices": len(vertices),
        "triangles": len(indices) // 3,
        "submeshes": [entry[0] if isinstance(entry, tuple) else entry.name for entry in submeshes],
        "hidden_materials": sorted(hidden_materials),
        "texture_sources": [os.path.basename(path) for path in texture_paths],
        "bounds": {"min": list(minimum), "max": list(maximum)},
        "renders": outputs,
    }


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io import import_skl, import_skn
    from Aventurine.utils.texture_manager import tex_to_dds_bytes

    rows = []
    for skin in [value.strip() for value in args.skins.split(",") if value.strip()]:
        rows.append(render_skin(args, skin, import_skl, import_skn, tex_to_dds_bytes))
    payload = {"status": "PASSED", "candidates": rows}
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(f"SOURCE_CANDIDATE_RENDERS=PASSED SKINS={len(rows)}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
