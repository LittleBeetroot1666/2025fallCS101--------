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
            start, stop, step = index.indices(n)
            length = len(range(start, stop, step))
            return [self.items[(start + i * step) % n] for i in range(length)]
        else:
            return self.items[index % n]

    def __setitem__(self, index, value):
        n = len(self.items)
        if n == 0:
            raise IndexError("Loop list is empty")

        if isinstance(index, slice):
            start, stop, step = index.indices(n)
            length = len(range(start, stop, step))
            val_iter = iter(value)
            for i in range(length):
                self.items[(start + i * step) % n] = next(val_iter)
        else:
            self.items[index % n] = value

    def __repr__(self):
        return f"Loop({self.items})"


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
            print(*js_lpf[j: j + m])
