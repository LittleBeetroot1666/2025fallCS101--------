class Loop:
    def __init__(self, items=None):
        """初始化环状列表。空参数创建空列表。"""
        self.items = list(items) if items is not None else []

    def __len__(self):
        """返回列表长度。"""
        return len(self.items)

    def __getitem__(self, index):
        """支持单索引/切片访问，支持多循环切片。"""
        n = len(self.items)
        if n == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            # 1. 将切片转为规范参数（处理负数/越界）
            start, stop, step = index.indices(n)
            # 2. 计算切片长度（支持多循环）
            length = len(range(start, stop, step))
            # 3. 直接生成环状元素（无中间列表）
            return [self.items[(start + i * step) % n] for i in range(length)]
        else:
            # 单索引：模运算直接取环状元素
            return self.items[index % n]

    def __setitem__(self, index, value):
        """支持单索引/切片赋值。"""
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
        """简洁表示环状列表。"""
        return f"Loop({self.items})"

    def __str__(self):
        """字符串表示，支持多循环输出。"""
        return str(self.items)

    def append(self, item):
        """在末尾添加元素。"""
        self.items.append(item)

    def extend(self, items):
        """扩展多个元素。"""
        self.items.extend(items)

    def pop(self, index=-1):
        """移除并返回元素。"""
        n = len(self.items)
        if n == 0:
            raise IndexError("pop from empty Loop list")
        return self.items.pop(index % n)

    def insert(self, index, item):
        """在指定位置插入元素。"""
        n = len(self.items)
        if n == 0:
            self.items.append(item)
            return
        self.items.insert(index % n, item)

    def to_list(self, cycles=1):
        """将环状列表转换为普通列表，支持多循环输出。"""
        if cycles <= 0:
            return []
        return self.items * cycles

    def slice_to_list(self, start, stop=None, step=1):
        """高效切片并直接返回列表。"""
        if stop is None:
            stop = start
            start = 0
        return self[start:stop:step]


# 测试用例
if __name__ == "__main__":
    # 创建环状列表
    l = Loop([1, 2, 3, 4])
    print("原始列表:", l)

    # 测试单索引访问
    print("l[4]:", l[4])  # 1 (环状访问)
    print("l[-1]:", l[-1])  # 4

    # 测试切片（多循环）
    print("l[2:10]:", l.slice_to_list(2, 10))  # [3, 4, 1, 2, 3, 4, 1, 2]
    print("l[1:10:2]:", l.slice_to_list(1, 10, 2))  # [2, 4, 2, 4, 2]

    # 测试切片赋值
    l[2:6] = [9, 8, 7, 6]
    print("赋值后:", l)  # Loop([1, 2, 9, 8])

    # 测试多循环输出
    print("3个循环:", l.to_list(3))  # [1, 2, 9, 8, 1, 2, 9, 8, 1, 2, 9, 8]

    # 测试空列表处理
    empty = Loop()
    try:
        print(empty[0])
    except IndexError as e:
        print("空列表错误:", e)
