import argparse
import hashlib
import json
import os
import sys
import tempfile

import bpy
from mathutils import Vector


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skn", required=True)
    parser.add_argument("--skl", required=True)
    parser.add_argument("--body-texture", required=True)
    parser.add_argument("--weapon-texture", required=True)
    parser.add_argument("--skirt-texture", required=True)
    parser.add_argument("--stock-animation", required=True)
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


def load_tex_image(path, tex_to_dds_bytes):
    descriptor, temporary = tempfile.mkstemp(suffix=".dds")
    os.close(descriptor)
    try:
        with open(temporary, "wb") as handle:
            handle.write(tex_to_dds_bytes(os.path.abspath(path)))
        image = bpy.data.images.load(temporary, check_existing=False)
        image.pack()
        image.colorspace_settings.name = "sRGB"
        return image
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)


def configure_material(material, image, transparent=False):
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    if transparent:
        shader.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 0.0)
        shader.inputs["Alpha"].default_value = 0.0
        material.surface_render_method = "DITHERED"
    else:
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        texture.interpolation = "Linear"
        shader.inputs["Roughness"].default_value = 0.62
        shader.inputs["Metallic"].default_value = 0.08
        shader.inputs["Specular IOR Level"].default_value = 0.34
        links.new(texture.outputs["Color"], shader.inputs["Base Color"])
        links.new(texture.outputs["Alpha"], shader.inputs["Alpha"])
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])


class Operator:
    def report(self, levels, message):
        print(f"AVENTURINE_{','.join(sorted(levels))}: {message}")


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io import import_anm, import_skl, import_skn
    from Aventurine.utils.texture_manager import tex_to_dds_bytes

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    joints, influences = import_skl.read_skl(os.path.abspath(args.skl))
    armature = import_skl.create_armature(joints, bone_orient="VISUAL")
    indices, vertices, submeshes = import_skn.read_skn(os.path.abspath(args.skn))
    mesh = import_skn.create_mesh(
        indices, vertices, submeshes, "Abyssal_Siren_Jinx", armature, joints, influences
    )
    armature.hide_render = True

    images = {
        "body": load_tex_image(args.body_texture, tex_to_dds_bytes),
        "weapon": load_tex_image(args.weapon_texture, tex_to_dds_bytes),
        "skirt": load_tex_image(args.skirt_texture, tex_to_dds_bytes),
    }
    for material in mesh.data.materials:
        name = material.name.lower()
        if "recall" in name:
            configure_material(material, images["body"], transparent=True)
        elif "weapon" in name:
            configure_material(material, images["weapon"])
        elif "skirt" in name:
            configure_material(material, images["skirt"])
        else:
            configure_material(material, images["body"])

    visible_vertex_indices = set()
    for polygon in mesh.data.polygons:
        material_name = mesh.data.materials[polygon.material_index].name.lower()
        if "recall" not in material_name:
            visible_vertex_indices.update(polygon.vertices)
    world_points = [
        mesh.matrix_world @ mesh.data.vertices[index].co for index in visible_vertex_indices
    ]
    minimum = Vector(tuple(min(point[i] for point in world_points) for i in range(3)))
    maximum = Vector(tuple(max(point[i] for point in world_points) for i in range(3)))
    target = (minimum + maximum) * 0.5
    extent = maximum - minimum
    distance = max(extent) * 2.4

    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 768
    scene.render.resolution_y = 768
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.world.color = (0.004, 0.008, 0.022)

    camera_data = bpy.data.cameras.new("QA_Camera")
    camera = bpy.data.objects.new("QA_Camera", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    camera_data.type = "ORTHO"

    add_area("Teal_Key", target + Vector((-2.4, -3.1, 3.2)), 1050, 3.8, (0.12, 1.0, 0.80), target)
    add_area("Violet_Rim", target + Vector((2.8, 2.7, 2.4)), 1250, 3.2, (0.72, 0.12, 1.0), target)
    add_area("Soft_Fill", target + Vector((2.2, -2.1, 1.0)), 680, 3.0, (0.32, 0.58, 1.0), target)

    os.makedirs(os.path.abspath(args.out_dir), exist_ok=True)
    views = {
        "front": target + Vector((0.0, -distance, 0.12 * extent.z)),
        "back": target + Vector((0.0, distance, 0.12 * extent.z)),
        "side": target + Vector((distance, 0.0, 0.12 * extent.z)),
    }
    rows = []
    for name, location in views.items():
        if name in {"front", "back"}:
            camera_data.ortho_scale = max(extent.z * 1.18, extent.x * 0.84)
        else:
            camera_data.ortho_scale = max(extent.z * 1.18, extent.y * 0.84)
        camera.location = location
        look_at(camera, target)
        output = os.path.abspath(os.path.join(args.out_dir, f"rest_{name}.png"))
        scene.render.filepath = output
        scene.frame_set(0)
        bpy.ops.render.render(write_still=True)
        rows.append({"view": name, "path": output, "sha256": sha256_file(output)})

    bpy.ops.object.select_all(action="DESELECT")
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    result = import_anm.load(
        Operator(),
        bpy.context,
        os.path.abspath(args.stock_animation),
        create_new_action=True,
        insert_frame=0,
        flip=False,
    )
    if "FINISHED" not in result:
        raise RuntimeError(f"ANM import failed: {result}")
    animation_frame = max(1, int(scene.frame_end) // 2)
    scene.frame_set(animation_frame)
    camera_data.ortho_scale = max(extent.z * 1.18, extent.x * 0.84)
    camera.location = views["front"]
    look_at(camera, target)
    animation_output = os.path.abspath(
        os.path.join(args.out_dir, f"stock_idle_front_f{animation_frame:03d}.png")
    )
    scene.render.filepath = animation_output
    bpy.ops.render.render(write_still=True)

    payload = {
        "status": "PASSED",
        "model": os.path.abspath(args.skn),
        "model_sha256": sha256_file(args.skn),
        "textures": {
            "body": sha256_file(args.body_texture),
            "weapon": sha256_file(args.weapon_texture),
            "skirt": sha256_file(args.skirt_texture),
        },
        "bounds": {"min": list(minimum), "max": list(maximum)},
        "resolution": [scene.render.resolution_x, scene.render.resolution_y],
        "rest_views": rows,
        "stock_animation_pose": {
            "path": os.path.abspath(args.stock_animation),
            "sha256": sha256_file(args.stock_animation),
            "frame": animation_frame,
            "render": animation_output,
            "render_sha256": sha256_file(animation_output),
            "packaged": False,
        },
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(f"ABYSSAL_QA_RENDER=PASSED REST_VIEWS={len(rows)} STOCK_POSE_VIEWS=1")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
