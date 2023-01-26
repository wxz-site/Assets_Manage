import bpy
from bpy.types import Operator,Panel,AddonPreferences

class LayoutDemoPanel(bpy.types.Panel):
    """在属性编辑器的场景上下文中创建一个面板"""
    bl_label = "Layout Demo"
    bl_idname = "AM_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

class Assets_Manage_Preferences(AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout


classes = (
    LayoutDemoPanel,
    Assets_Manage_Preferences,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

