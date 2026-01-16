# utils.py
import os
import sys

def resource_path(relative_path):
    """获取资源的绝对路径，兼容 PyInstaller 打包和源码运行"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
