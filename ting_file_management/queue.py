class Queue:
    def __init__(self):
        self.__data = []

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
