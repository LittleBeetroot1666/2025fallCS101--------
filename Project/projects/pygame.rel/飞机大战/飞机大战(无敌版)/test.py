import os

def print_structure(start_path, indent=''):
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        print(indent + '|-- ' + item)
        if os.path.isdir(item_path):
            print_structure(item_path, indent + '    ')

# 修改为你的项目根目录路径，例如：
# project_path = "E:/COM/game/feiji"
project_path = os.getcwd()  # 当前目录
print("项目文件结构：")
print_structure(project_path)
