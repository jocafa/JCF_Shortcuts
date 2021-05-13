bl_info = {
    "name": "Jocafa Shortcuts",
    "description": "Jocafa's Shortcuts",
    "author": "Josh Faul",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "3D View > Sidebar",
    "warning": "",
    "category": "3D View"
}

import bpy

#import panels
from .panels import JCF_ShortcutsPanel

#import operators
from .operators import (
    JCF_OT_set_render_size,
    JCF_OT_set_render_scale,
    JCF_OT_set_render_samples,
    JCF_OT_add_tetrasphere,
    JCF_OT_debug
)

#shared properties
class JCF_Properties(bpy.types.PropertyGroup):
    """JCF Shared Properties"""
    overlays_expanded: bpy.props.BoolProperty(default=True)
    foo: bpy.props.FloatProperty(name="foo", default=0.0, min=0.0, max=1.0)

classes = (
    JCF_Properties,
    JCF_ShortcutsPanel,
    JCF_OT_set_render_size,
    JCF_OT_set_render_scale,
    JCF_OT_set_render_samples,
    JCF_OT_add_tetrasphere,
    JCF_OT_debug
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.jcf_props = bpy.props.PointerProperty(type=JCF_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.jcf_props


if __name__ == "__main__":
    register()
