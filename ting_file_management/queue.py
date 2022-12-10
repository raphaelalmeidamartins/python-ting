class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self):
            return self._data.pop(0)
        return None

    def search(self, index):
        if 0 <= index < len(self):
            return self._data[index]
        raise IndexError("Index out of range")
