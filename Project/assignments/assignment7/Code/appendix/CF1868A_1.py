class Loopify:
    def __init__(self, items=None):
        """初始化环状列表。如果未提供参数，则创建空列表。"""
        self.items = list(items) if items is not None else []

    def __len__(self):
        """返回列表的长度。"""
        return len(self.items)

    def __getitem__(self, index):
        """通过索引获取元素，支持环状访问。"""
        if not self.items:
            raise IndexError("Loop list is empty")
        # 计算实际索引位置（处理负索引和越界）
        return self.items[index % len(self.items)]

    def __setitem__(self, index, value):
        """通过索引设置元素，支持环状访问。"""
        if not self.items:
            raise IndexError("Loop list is empty")
        # 计算实际索引位置（处理负索引和越界）
        self.items[index % len(self.items)] = value

    def __repr__(self):
        """返回环状列表的字符串表示。"""
        return f"Loop({self.items})"

    def append(self, item):
        """在列表末尾添加元素。"""
        self.items.append(item)

    def extend(self, items):
        """扩展列表，添加多个元素。"""
        self.items.extend(items)

    def pop(self, index=-1):
        """移除并返回指定位置的元素（默认最后一个）。"""
        return self.items.pop(index % len(self.items) if self.items else 0)


