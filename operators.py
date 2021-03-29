import bpy

from . import constants as const

class JCF_OT_debug(bpy.types.Operator):
    """Breakpoint for debugging and inspecting"""

    bl_idname = "jcf.debug"
    bl_label = "Debug"
    bl_options = {'REGISTER'}

    def execute(self, context):
        data = bpy.data
        print("JCF DEBUG")
        return {'FINISHED'}

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

class JCF_OT_add_tetrasphere(bpy.types.Operator):
    """Create a subdivided tetrahedron sphere"""

    bl_idname = "jcf.add_tetrasphere"
    bl_label = "Tetrasphere"
    bl_options = {'REGISTER'}

    def execute(self, context):
        """
            create solid
            auto smooth: 30deg
            shade smooth

            Subdiv - levels: 4, render levels: 4, quality: 6, use limit surface: True
            Cast - type: sphere, factor: 1, size: 1, use radius as size: False

            -- Apply --

            Add vertex groups: Cuts, Rim, Shell
            Assign interleaved branches to cuts

            Mask - vertex group: cuts inverted, threshold: 0.999
            Subdiv - levels: 3, render levels: 3, quality: 6, use limit surface: True
            Cast - type: sphere, factor: 1, size: 1, use radius as size: False
            Solidify - thickness: 10cm, offset: -1, even thickness: True, rim fill: True, high quality normals: true, vertex groups: shell/rim
            Bevel - edges, type: offset, amount: 1cm, segments: 1, limit method: angle, angle: 30deg, harden normals: true
            Bevel - edges, type: offset, amount: 1mm, segments: 1, limit method: angle, angle: 30deg, harden normals: true
        """

        bpy.ops.mesh.primitive_solid_add()
        ao = bpy.context.active_object
        if ao:
            subsurf = ao.modifiers.new(name="Subdivision", type='SUBSURF')
            subsurf.levels = 3
            subsurf.render_levels = 3
            subsurf.quality = 6
            subsurf.use_limit_surface = True
            subsurf.show_only_control_edges = False

            cast = ao.modifiers.new(name="Cast", type='CAST')
            cast.factor = 1
            cast.size = 1
            cast.use_radius_as_size = False

        return {'FINISHED'}