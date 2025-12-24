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


