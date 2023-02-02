from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self.__iterable = iterable
        self.index = 0

    def __next__(self):
        try:
            data = self.__iterable[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return data
