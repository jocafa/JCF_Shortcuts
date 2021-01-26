import bpy

from . import constants as const
from . import operators as ops

class JCF_ShortcutsPanel(bpy.types.Panel):
    """Jocafa Shortcuts Panel"""
    bl_label = "Jocafa Shortcuts"
    bl_idname = "JCF_PT_jcf_shortcuts"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "objectmode"
    bl_category = "Jocafa"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Camera", icon='CAMERA_DATA')
        row = layout.row(align=True)
        row.prop(scene.camera.data.dof, "use_dof")
        row.prop(scene.camera_settings, "enable_ae")

        row = layout.row()
        row.prop(scene.view_settings, "exposure")

        row = layout.row()
        row.prop(scene.camera.data, "lens")

        row = layout.row()
        row.prop(scene.camera.data.dof, "focus_distance")

        row = layout.row()
        row.prop(scene.camera.data.dof, "aperture_fstop")

        layout.separator()

        layout.label(text="Resolution & Scale", icon='OUTPUT')
        row=layout.row(align=True)

        # Quick list of resolutions
        i = 0
        for res in const.resolutions:
            row.operator(ops.JCF_OT_set_render_size.bl_idname, text=res['name']).index = i
            i+=1

        # Quick list of scales
        row=layout.row(align=True)
        for s in const.scales:
            row.operator(ops.JCF_OT_set_render_scale.bl_idname, text=s[0]).scale = s[1] * 100

        layout.separator()

        # HDRI Sun Aligner shortcuts
        layout.label(text="HDRI Sun Aligner", icon='LIGHT_SUN')
        row=layout.row(align=True)
        row.operator('hdrisa.dummy', text="Sun Position")
        row.operator('hdrisa.rotate', text="Rotate Active")
