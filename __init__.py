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

from . import constants as const

#import panels
from .panels import JCF_ShortcutsPanel

#import operators
from .operators import JCF_OT_set_render_size
from .operators import JCF_OT_set_render_scale

#shared properties
class JCF_Properties(bpy.types.PropertyGroup):
    """JCF Shared Properties"""
    foo: bpy.props.FloatProperty(name="foo", default=0.0, min=0.0, max=1.0)

classes = (
    JCF_Properties,
    JCF_ShortcutsPanel,
    JCF_OT_set_render_size,
    JCF_OT_set_render_scale
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
