# 此示例脚本演示了如何在按钮或菜单项上放置自定义图标.
# 重要说明：如果您直接运行此示例，则按钮中将没有图标 
# 您需要将图像路径替换为真实的图像路径.
# 对于可分发脚本，建议将图标放置在addon文件夹中，并相对于py脚本文件进行访问，以实现可移植性。
#
#
# UI预览的其他用例:
# - 提供固定的预览列表以供选择
# - 提供预览的动态列表 (eg. 通过读取目录计算得出)
#
# 对于以上用例，请参见模板 'ui_previews_dynamic_enum.py"


import os
import bpy


class PreviewsExamplePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Previews Example Panel"
    bl_idname = "OBJECT_PT_previews"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        pcoll = preview_collections["main"]

        row = layout.row()
        my_icon = pcoll["my_icon"]
        row.operator("render.render", icon_value=my_icon.icon_id)

        # my_icon.icon_id 可以在任何接受以下功能的UI函数中使用
        # icon_value # 也尝试设置 text="" 来获得仅图标操作员按钮
# 我们可以在这里存储多个预览集合,
# 但是在这个例子中我们只存储 "main"
preview_collections = {}

def register():

    # 请注意，由bpy.utils.previews返回的预览集合 
    # 是常规的py对象-您可以使用它们存储自定义数据.
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # 该图标所在的文件夹的路径是相对于addon文件夹中的该py文件计算的
    # 
    my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    # 加载文件的预览缩略图并存储在预览集合中
    pcoll.load("my_icon", os.path.join(my_icons_dir, "icon-image.png"), 'IMAGE')

    preview_collections["main"] = pcoll

    bpy.utils.register_class(PreviewsExamplePanel)


def unregister():

    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

    bpy.utils.unregister_class(PreviewsExamplePanel)


if __name__ == "__main__":
    register()