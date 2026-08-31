import argparse
import hashlib
import json
import os
import sys
import tempfile

import bpy
import numpy as np
from mathutils import Vector

from project_version import VERSION


CHAMPION_TEXTURE_ROUTES = {
    "WitchBody": "body",
    "CoralArmor": "armor",
    "PowPow": "weapon",
    "Fishbones": "weapon",
    "Zapper": "weapon",
    "Recall": "recall",
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skn", required=True)
    parser.add_argument("--skl", required=True)
    parser.add_argument("--body-texture", required=True)
    parser.add_argument("--armor-texture", required=True)
    parser.add_argument("--weapon-texture", required=True)
    parser.add_argument("--recall-texture", required=True)
    parser.add_argument("--mine-skn", required=True)
    parser.add_argument("--mine-skl", required=True)
    parser.add_argument("--mine-texture", required=True)
    parser.add_argument("--missile-skn", required=True)
    parser.add_argument("--missile-skl", required=True)
    parser.add_argument("--missile-texture", required=True)
    parser.add_argument("--minigun-animation", required=True)
    parser.add_argument("--rocket-animation", required=True)
    parser.add_argument("--zapper-animation", required=True)
    parser.add_argument("--recall-animation", required=True)
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


def reset_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (
        bpy.data.meshes,
        bpy.data.armatures,
        bpy.data.materials,
        bpy.data.images,
        bpy.data.lights,
        bpy.data.cameras,
    ):
        for datablock in list(datablocks):
            if datablock.users == 0:
                datablocks.remove(datablock)


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


def configure_material(material, image, visible=True, emissive=0.0):
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    if not visible:
        shader.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 0.0)
        shader.inputs["Alpha"].default_value = 0.0
        material.surface_render_method = "DITHERED"
    else:
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = image
        texture.interpolation = "Linear"
        shader.inputs["Roughness"].default_value = 0.70
        shader.inputs["Metallic"].default_value = 0.04
        shader.inputs["Specular IOR Level"].default_value = 0.30
        links.new(texture.outputs["Color"], shader.inputs["Base Color"])
        if emissive > 0:
            links.new(texture.outputs["Color"], shader.inputs["Emission Color"])
            shader.inputs["Emission Strength"].default_value = emissive
    links.new(shader.outputs["BSDF"], output.inputs["Surface"])


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


def scene_setup(target, extent):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 900
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.render.image_settings.color_depth = "8"
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.world.color = (0.003, 0.004, 0.012)
    camera_data = bpy.data.cameras.new("QA_Camera")
    camera = bpy.data.objects.new("QA_Camera", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    camera_data.type = "ORTHO"
    span = max(extent)
    # Blender area-light power is absolute while the light size and distance
    # below scale with the object.  Scale watts as well so small props are not
    # overexposed relative to the champion.
    light_scale = max((span / 2.4) ** 2, 0.08)
    # Keep the QA render close to neutral Summoner's Rift illumination.  Strong
    # coral/seafoam lights hid the actual atlas values and made dark props look
    # pastel, which defeats the purpose of validating exported textures.
    add_area(
        "Neutral_Key",
        target + Vector((-span * 0.9, -span * 1.1, span * 1.2)),
        780 * light_scale,
        span * 1.4,
        (0.86, 0.90, 1.0),
        target,
    )
    add_area(
        "Seafoam_Rim",
        target + Vector((span * 1.0, span * 0.9, span * 0.75)),
        360 * light_scale,
        span * 1.2,
        (0.18, 1.0, 0.73),
        target,
    )
    add_area(
        "Coral_Fill",
        target + Vector((span * 0.65, -span * 0.7, span * 0.2)),
        300 * light_scale,
        span * 1.1,
        (1.0, 0.12, 0.32),
        target,
    )
    return scene, camera, camera_data


def object_bounds(mesh, excluded_materials=()):
    excluded = {name.lower() for name in excluded_materials}
    indices = set()
    for polygon in mesh.data.polygons:
        material = mesh.data.materials[polygon.material_index]
        if material and material.name.lower() not in excluded:
            indices.update(polygon.vertices)
    if not indices:
        indices = set(range(len(mesh.data.vertices)))
    points = [mesh.matrix_world @ mesh.data.vertices[index].co for index in indices]
    minimum = Vector(tuple(min(point[axis] for point in points) for axis in range(3)))
    maximum = Vector(tuple(max(point[axis] for point in points) for axis in range(3)))
    return minimum, maximum


def material_bounds(mesh, material_names):
    wanted = {name.lower() for name in material_names}
    indices = set()
    for polygon in mesh.data.polygons:
        material = mesh.data.materials[polygon.material_index]
        if material and material.name.lower() in wanted:
            indices.update(polygon.vertices)
    if not indices:
        raise ValueError(f"No polygons found for material bounds: {sorted(wanted)}")
    points = [mesh.matrix_world @ mesh.data.vertices[index].co for index in indices]
    minimum = Vector(tuple(min(point[axis] for point in points) for axis in range(3)))
    maximum = Vector(tuple(max(point[axis] for point in points) for axis in range(3)))
    return minimum, maximum


def render_view(scene, camera, camera_data, output, target, location, ortho_scale):
    camera.location = location
    camera_data.ortho_scale = ortho_scale
    look_at(camera, target)
    scene.render.filepath = os.path.abspath(output)
    bpy.ops.render.render(write_still=True)
    return {
        "path": os.path.abspath(output),
        "sha256": sha256_file(output),
        "frame": int(scene.frame_current),
        "camera_target": list(target),
        "ortho_scale": float(ortho_scale),
    }


class Operator:
    def report(self, levels, message):
        print(f"AVENTURINE_{','.join(sorted(levels))}: {message}")


def load_action(import_anm, armature, animation):
    armature.animation_data_clear()
    bpy.ops.object.select_all(action="DESELECT")
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    result = import_anm.load(
        Operator(),
        bpy.context,
        os.path.abspath(animation),
        create_new_action=True,
        insert_frame=0,
        flip=False,
    )
    if "FINISHED" not in result:
        raise RuntimeError(f"ANM import failed: {animation}: {result}")


def render_champion(args, import_skl, import_skn, import_anm, tex_to_dds_bytes):
    reset_scene()
    joints, influences = import_skl.read_skl(os.path.abspath(args.skl))
    armature = import_skl.create_armature(joints, bone_orient="VISUAL")
    indices, vertices, submeshes = import_skn.read_skn(os.path.abspath(args.skn))
    names = [submesh.name for submesh in submeshes]
    if names != list(CHAMPION_TEXTURE_ROUTES):
        raise ValueError(f"Unexpected champion submeshes: {names}")
    mesh = import_skn.create_mesh(
        indices, vertices, submeshes, "Abyssal_Sea_Witch_Jinx", armature, joints, influences
    )
    armature.hide_render = True
    images = {
        "body": load_tex_image(args.body_texture, tex_to_dds_bytes),
        "armor": load_tex_image(args.armor_texture, tex_to_dds_bytes),
        "weapon": load_tex_image(args.weapon_texture, tex_to_dds_bytes),
        "recall": load_tex_image(args.recall_texture, tex_to_dds_bytes),
    }
    material_by_name = {material.name: material for material in mesh.data.materials}
    for name, role in CHAMPION_TEXTURE_ROUTES.items():
        configure_material(
            material_by_name[name], images[role], visible=name != "Recall", emissive=0.08
        )
    minimum, maximum = object_bounds(mesh, excluded_materials={"Recall"})
    target = (minimum + maximum) * 0.5
    extent = maximum - minimum
    distance = max(extent) * 2.5
    scene, camera, camera_data = scene_setup(target, extent)
    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)
    full_scale = max(extent.z * 1.20, extent.x * 1.32, extent.y * 1.32)
    rest_views = {}
    views = {
        "front": target + Vector((0.0, -distance, extent.z * 0.10)),
        "front_three_quarter": target + Vector((distance * 0.72, -distance * 0.72, extent.z * 0.12)),
        "left": target + Vector((-distance, 0.0, extent.z * 0.10)),
        "right": target + Vector((distance, 0.0, extent.z * 0.10)),
        "back": target + Vector((0.0, distance, extent.z * 0.10)),
    }
    scene.frame_set(0)
    for label, location in views.items():
        output = os.path.join(out_dir, f"model_rest_{label}.png")
        rest_views[label] = render_view(
            scene, camera, camera_data, output, target, location, full_scale
        )

    head_index = next(index for index, joint in enumerate(joints) if joint.name == "Head")
    head_target = armature.matrix_world @ joints[head_index].global_pos
    face_output = os.path.join(out_dir, "model_face_crown_closeup.png")
    face_closeup = render_view(
        scene,
        camera,
        camera_data,
        face_output,
        head_target + Vector((0.0, 0.0, 0.06)),
        head_target + Vector((1.7, -2.1, 0.7)),
        0.92,
    )

    weapon_min, weapon_max = material_bounds(mesh, {"PowPow", "Fishbones", "Zapper"})
    weapon_target = (weapon_min + weapon_max) * 0.5
    weapon_extent = weapon_max - weapon_min
    weapon_output = os.path.join(out_dir, "model_coral_relic_weapons_closeup.png")
    weapon_closeup = render_view(
        scene,
        camera,
        camera_data,
        weapon_output,
        weapon_target,
        weapon_target + Vector((max(weapon_extent) * 1.8, -max(weapon_extent) * 2.0, max(weapon_extent) * 0.55)),
        max(weapon_extent) * 1.25,
    )

    pose_specs = (
        ("stock_minigun_idle", args.minigun_animation, 0.53, False),
        ("stock_rocket_idle", args.rocket_animation, 0.56, False),
        ("stock_zapper_spell2", args.zapper_animation, 0.47, False),
        ("stock_recall", args.recall_animation, 0.62, True),
    )
    poses = {}
    for label, animation, fraction, show_recall in pose_specs:
        configure_material(
            material_by_name["Recall"], images["recall"], visible=show_recall, emissive=0.12
        )
        load_action(import_anm, armature, animation)
        frame_end = max(1, int(scene.frame_end))
        frame = max(1, min(frame_end, int(round(frame_end * fraction))))
        scene.frame_set(frame)
        output = os.path.join(out_dir, f"model_{label}_f{frame:03d}.png")
        row = render_view(
            scene,
            camera,
            camera_data,
            output,
            target,
            target + Vector((0.0, -distance, extent.z * 0.10)),
            full_scale,
        )
        row.update(
            {
                "animation": os.path.abspath(animation),
                "animation_sha256": sha256_file(animation),
                "show_recall": show_recall,
                "packaged": False,
            }
        )
        poses[label] = row
    configure_material(material_by_name["Recall"], images["recall"], visible=False)
    scene.frame_set(0)
    return {
        "model": os.path.abspath(args.skn),
        "model_sha256": sha256_file(args.skn),
        "vertices": len(vertices),
        "triangles": len(indices) // 3,
        "submeshes": names,
        "bounds": {"min": list(minimum), "max": list(maximum)},
        "rest_views": rest_views,
        "face_closeup": face_closeup,
        "weapon_closeup": weapon_closeup,
        "stock_animation_poses": poses,
    }


def render_prop(
    label,
    skn_path,
    skl_path,
    texture_path,
    import_skl,
    import_skn,
    tex_to_dds_bytes,
    out_dir,
    manual_open=False,
):
    reset_scene()
    joints, influences = import_skl.read_skl(os.path.abspath(skl_path))
    armature = import_skl.create_armature(joints, bone_orient="VISUAL")
    indices, vertices, submeshes = import_skn.read_skn(os.path.abspath(skn_path))
    mesh = import_skn.create_mesh(
        indices, vertices, submeshes, f"Sea_Witch_{label}", armature, joints, influences
    )
    armature.hide_render = True
    image = load_tex_image(texture_path, tex_to_dds_bytes)
    for material in mesh.data.materials:
        configure_material(material, image, visible=True, emissive=0.10)
    minimum, maximum = object_bounds(mesh)
    target = (minimum + maximum) * 0.5
    extent = maximum - minimum
    distance = max(extent) * 2.8
    scene, camera, camera_data = scene_setup(target, extent)
    scene.frame_set(0)
    output = os.path.join(os.path.abspath(out_dir), f"model_{label}_three_quarter.png")
    rest = render_view(
        scene,
        camera,
        camera_data,
        output,
        target,
        target + Vector((distance * 0.72, -distance * 0.72, max(extent) * 0.35)),
        max(extent) * 1.45,
    )
    opened = None
    if manual_open:
        for bone in armature.pose.bones:
            if bone.name == "Jaw_Top":
                bone.rotation_mode = "XYZ"
                bone.rotation_euler.x = -0.42
            elif bone.name == "Jaw_Bot":
                bone.rotation_mode = "XYZ"
                bone.rotation_euler.x = 0.42
        bpy.context.view_layer.update()
        output = os.path.join(os.path.abspath(out_dir), f"model_{label}_manual_jaw_test.png")
        opened = render_view(
            scene,
            camera,
            camera_data,
            output,
            target,
            target + Vector((distance * 0.72, -distance * 0.72, max(extent) * 0.35)),
            max(extent) * 1.45,
        )
        opened["manual_pose_not_packaged"] = True
    return {
        "model": os.path.abspath(skn_path),
        "model_sha256": sha256_file(skn_path),
        "vertices": len(vertices),
        "triangles": len(indices) // 3,
        "submeshes": [submesh.name for submesh in submeshes],
        "texture_sha256": sha256_file(texture_path),
        "rest": rest,
        "manual_deformation_test": opened,
    }


def write_contact_sheet(image_paths, output):
    loaded = []
    for path in image_paths:
        image = bpy.data.images.load(os.path.abspath(path), check_existing=False)
        width, height = map(int, image.size)
        pixels = np.empty(width * height * 4, dtype=np.float32)
        image.pixels.foreach_get(pixels)
        rgba = np.clip(np.rint(pixels.reshape(height, width, 4) * 255.0), 0, 255).astype(
            np.uint8
        )
        loaded.append(rgba)
        bpy.data.images.remove(image)
    thumb = 450
    columns = 3
    rows = (len(loaded) + columns - 1) // columns
    canvas = np.zeros((rows * thumb, columns * thumb, 4), dtype=np.uint8)
    canvas[..., 3] = 255
    for index, rgba in enumerate(loaded):
        y = index // columns * thumb
        x = index % columns * thumb
        step_y = max(1, rgba.shape[0] // thumb)
        step_x = max(1, rgba.shape[1] // thumb)
        sampled = rgba[::step_y, ::step_x][:thumb, :thumb]
        canvas[y : y + sampled.shape[0], x : x + sampled.shape[1]] = sampled
    image = bpy.data.images.new("Sea_Witch_QA_Contact_Sheet", canvas.shape[1], canvas.shape[0], alpha=True)
    image.pixels.foreach_set(canvas.astype(np.float32).reshape(-1) / 255.0)
    image.filepath_raw = os.path.abspath(output)
    image.file_format = "PNG"
    image.save()
    bpy.data.images.remove(image)
    return {"path": os.path.abspath(output), "sha256": sha256_file(output)}


def main():
    args = parse_args()
    sys.path.insert(0, os.path.abspath(args.addon_root))
    from Aventurine.io import import_anm, import_skl, import_skn
    from Aventurine.utils.texture_manager import tex_to_dds_bytes

    champion = render_champion(
        args, import_skl, import_skn, import_anm, tex_to_dds_bytes
    )
    chompers = render_prop(
        "chompers",
        args.mine_skn,
        args.mine_skl,
        args.mine_texture,
        import_skl,
        import_skn,
        tex_to_dds_bytes,
        args.out_dir,
        manual_open=True,
    )
    missile = render_prop(
        "leviathan_missile",
        args.missile_skn,
        args.missile_skl,
        args.missile_texture,
        import_skl,
        import_skn,
        tex_to_dds_bytes,
        args.out_dir,
        manual_open=False,
    )
    selected = [
        champion["rest_views"]["front"]["path"],
        champion["rest_views"]["front_three_quarter"]["path"],
        champion["rest_views"]["back"]["path"],
        champion["face_closeup"]["path"],
        champion["weapon_closeup"]["path"],
        champion["stock_animation_poses"]["stock_minigun_idle"]["path"],
        champion["stock_animation_poses"]["stock_rocket_idle"]["path"],
        champion["stock_animation_poses"]["stock_zapper_spell2"]["path"],
        champion["stock_animation_poses"]["stock_recall"]["path"],
        chompers["rest"]["path"],
        chompers["manual_deformation_test"]["path"],
        missile["rest"]["path"],
    ]
    contact_sheet = write_contact_sheet(
        selected, os.path.join(os.path.abspath(args.out_dir), "sea_witch_model_contact_sheet.png")
    )
    payload = {
        "status": "PASSED",
        "version": VERSION,
        "render_source": "exported SKN/TEX outputs",
        "resolution": [900, 900],
        "champion": champion,
        "chompers": chompers,
        "ultimate_missile": missile,
        "contact_sheet": contact_sheet,
        "manual_visual_review_required": True,
        "live_game_test_completed": False,
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
    with open(args.report, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(
        "SEA_WITCH_VISUAL_QA=PASSED REST_VIEWS=5 STOCK_POSES=4 "
        "PROP_RENDERS=3 CONTACT_SHEET=1"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)
