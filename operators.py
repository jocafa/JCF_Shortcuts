import bpy

from . import constants as const

class JCF_OT_set_render_size(bpy.types.Operator):
    """Set Render Size"""

    bl_idname = "jcf.set_render_size"
    bl_label = "Set Render Size"
    bl_options = {'REGISTER'}

    index: bpy.props.IntProperty(default=0)

    def execute(self, context):
        bpy.context.scene.render.resolution_x = const.resolutions[self.index]['width']
        bpy.context.scene.render.resolution_y = const.resolutions[self.index]['height']
        return {'FINISHED'}

class JCF_OT_set_render_scale(bpy.types.Operator):
    """Set Render Size"""

    bl_idname = "jcf.set_render_scale"
    bl_label = "Set Render Scale"
    bl_options = {'REGISTER'}

    scale: bpy.props.FloatProperty(default=100.0)

    def execute(self, context):
        bpy.context.scene.render.resolution_percentage = self.scale
        return {'FINISHED'}
