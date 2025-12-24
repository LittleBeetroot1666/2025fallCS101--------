class Loop:
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

    def __str__(self):
        return str(self.items)

    def append(self, item):
        self.items.append(item)

    def extend(self, items):
        self.items.extend(items)

    def pop(self, index=-1):
        n = len(self.items)
        if n == 0:
            raise IndexError("pop from empty Loop list")
        return self.items.pop(index % n)

    def insert(self, index, item):
        n = len(self.items)
        if n == 0:
            self.items.append(item)
            return
        self.items.insert(index % n, item)

    def to_list(self, cycles=1):
        if cycles <= 0:
            return []
        return self.items * cycles

    def slice_to_list(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        return self[start:stop:step]



