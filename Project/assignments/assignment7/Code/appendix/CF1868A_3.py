class Loopify:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        n0 = len(self.items)
        if n0 == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            start, stop, step = index.indices(n0)
            length = len(range(start, stop, step))
            return Loopify([self.items[(start + i * step) % n0] for i in range(length)])
        else:
            return self.items[index % n0]

    def __setitem__(self, index, value):
        n0 = len(self.items)
        if n0 == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            start, stop, step = index.indices(n0)
            length = len(range(start, stop, step))
            val_iter = iter(value)
            for i in range(length):
                self.items[(start + i * step) % n0] = next(val_iter)
        else:
            self.items[index % n0] = value

    def __repr__(self):
        return f"Loop({self.items})"

    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def pop(self, index=-1):
        n0 = len(self.items)
        return self.items.pop(index % n0) if n0 else _empty_err()

    def insert(self, index, item):
        n0 = len(self.items)
        self.items.insert(index % n0 if n0 else 0, item)


def _empty_err():
    raise IndexError("pop from empty Loop list")


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if m == 1:
        for _ in range(n + 1):
            print(0)
    else:
        print(min(n + 1, m))
        js_lpf = Loopify([str(i) for i in range(m)])
        for j in range(n):
            print(js_lpf[j: j + m])
