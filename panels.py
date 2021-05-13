import bpy

from . import constants as const
from . import operators as ops

class JCF_RenderShortcutsPanel(bpy.types.Panel):
    """Jocafa Render Shortcuts Panel"""
    bl_label = "Jocafa Render Shortcuts"
    bl_idname = "JCF_PT_jcf_render_shortcuts"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "render"
    bl_category = "Jocafa"

    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="SOLO_ON")
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout

        row = layout.row(align = True)

        # Camera Shortcuts
        layout.label(text="Camera", icon='CAMERA_DATA')
        row = layout.row(align=True)
        row.prop(scene.camera.data.dof, "use_dof", text="DOF")
        row.prop(scene.camera_settings, "enable_ae", text="AE")
        row.prop(scene.view_settings, "exposure")

        row = layout.row(align=True)
        row.prop(scene.camera.data, "lens", text="Lens", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        row.prop(scene.camera.data.dof, "focus_distance", text="Dist", icon='DRIVER_DISTANCE')
        row.prop(scene.camera.data.dof, "aperture_fstop", text="F-Stop", icon='PROP_ON')

        layout.separator()

        layout.label(text="Resolution, Scale, and Sampling", icon='OUTPUT')
        row = layout.row(align=True)

        # Quick list of resolutions
        i = 0
        for res in const.resolutions:
            row.operator(ops.JCF_OT_set_render_size.bl_idname, text=res['name']).index = i
            i += 1

        # Quick list of scales
        row = layout.row(align=True)
        for s in const.scales:
            row.operator(ops.JCF_OT_set_render_scale.bl_idname, text=s[0]).scale = s[1] * 100

        row = layout.row(align=True)
        for s in const.samples:
            row.operator(ops.JCF_OT_set_render_samples.bl_idname, text=s['name']).samples = s['value']

        # Compositing
        row = layout.row(align=True)
        row.prop(scene.render, "use_compositing")
        row.prop(scene.render, "use_sequencer")

        layout.separator()

        # HDRI Sun Aligner shortcuts
        layout.label(text="HDRI Sun Aligner", icon='LIGHT_SUN')
        row = layout.row(align=True)
        row.operator('hdrisa.dummy', text="Sun Position")
        row.operator('hdrisa.rotate', text="Rotate Active")


class JCF_ShortcutsPanel(bpy.types.Panel):
    """Jocafa Shortcuts Panel"""
    bl_label = "Jocafa Shortcuts"
    bl_idname = "JCF_PT_jcf_shortcuts"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = "objectmode"
    bl_category = "Jocafa"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        jcf_props = scene.jcf_props
        overlay = context.space_data.overlay
        shading = context.space_data.shading

        # Viewport overlay shortcuts
        box = layout.box()
        row = box.row()
        row.prop(
            jcf_props,
            "overlays_expanded",
            icon='TRIA_DOWN' if jcf_props.overlays_expanded else 'TRIA_RIGHT',
            icon_only=True,
            emboss=False
        )
        row.label(text="Viewport Overlays", icon='OVERLAY')

        if jcf_props.overlays_expanded:
            row = box.row(align=True)
            row.prop(overlay, "show_wireframes", text="")
            row.prop(overlay, "wireframe_threshold", text="Wireframe")

            row = box.row(align=True)
            row.prop(overlay, "show_vertex_normals", text="", icon='NORMALS_VERTEX')
            row.prop(overlay, "show_split_normals", text="", icon='NORMALS_VERTEX_FACE')
            row.prop(overlay, "show_face_normals", text="", icon='NORMALS_FACE')
            row.prop(overlay, "normals_length", text="Size")

            row = box.row(align=True)
            row.prop(overlay, "show_face_orientation", text="Face Orientation")

            row = box.row(align=True)
            row.prop(shading, "show_xray", text="")
            row.prop(shading, "xray_alpha", text="X-Ray")

        layout.separator()

        # Quick Objects
        layout.label(text="Quick Objects", icon='MESH_MONKEY')
        row = layout.row();
        row.operator(ops.JCF_OT_add_tetrasphere.bl_idname)

        #layout.separator()

        # DEBUGGING
        #layout.label(text="DEBUG", icon='TOOL_SETTINGS')
        #row = layout.row();
        #row.operator(ops.JCF_OT_debug.bl_idname)
