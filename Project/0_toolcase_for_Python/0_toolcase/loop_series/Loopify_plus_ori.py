# 生成环状列表
class Loopify:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        n = len(self.items)
        if n == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            # 1. 将切片转为规范参数（处理负数/越界）
            start, stop, step = index.indices(n)
            # 2. 计算切片长度（直接用range的长度，天然支持多循环）
            length = len(range(start, stop, step))
            # 3. 生成环状元素（无中间列表，直接计算索引）
            return Loopify([self.items[(start + i * step) % n] for i in range(length)])
        else:
            # 单索引：模运算实现环状
            return self.items[index % n]

    def __setitem__(self, index, value):
        n = len(self.items)
        if n == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            start, stop, step = index.indices(n)
            length = len(range(start, stop, step))
            # 批量赋值（value需匹配切片长度）
            val_iter = iter(value)
            for i in range(length):
                self.items[(start + i * step) % n] = next(val_iter)
        else:
            self.items[index % n] = value

    def __repr__(self):
        return f"Loop({self.items})"

    # 常用列表方法（保持原生体验）
    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def pop(self, index=-1):
        n = len(self.items)
        return self.items.pop(index % n) if n else _empty_err()

    def insert(self, index, item):
        n = len(self.items)
        self.items.insert(index % n if n else 0, item)


def _empty_err():
    raise IndexError("pop from empty Loop list")

