class Loopify:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if not self.items:
            raise IndexError("Loop list is empty")

        return self.items[index % len(self.items)]

    def __setitem__(self, index, value):
        if not self.items:
            raise IndexError("Loop list is empty")
        self.items[index % len(self.items)] = value

    def __repr__(self):
        return f"Loop({self.items})"

    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def pop(self, index=-1):
        return self.items.pop(index % len(self.items) if self.items else 0)


n, m = list(map(int, input().split()))
if m == 1:
    for _ in range(n + 1):
        print(0)
else:
    print(min(n + 1, m))
    js_lpf = Loopify([str(i) for i in range(m)])
    for j in range(n):
        print(' '.join(js_lpf[j: j + m]))
        