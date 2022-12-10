from collections.abc import Iterator, Iterable


class QueueIterator(Iterator):
    def __init__(self, queue):
        self.__queue = queue
        self.__index = 0

    def __next__(self):
        try:
            current_item = self.__queue.search(self.__index)
        except IndexError:
            raise StopIteration()
        else:
            self.__index += 1
            return current_item


class Queue(Iterable):
    def __init__(self):
        self.__data = []

    def __iter__(self):
        return QueueIterator(self)

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if len(self):
            return self.__data.pop(0)
        return None

    def search(self, index):
        if 0 <= index < len(self):
            return self.__data[index]
        raise IndexError("Index out of range")
