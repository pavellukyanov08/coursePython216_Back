from random import randint
from abc import ABC, abstractmethod


class ArrayOperations(ABC):
    @abstractmethod
    def do_something(self, array):
        pass


class DisplayMax(ArrayOperations):
    def do_something(self, array):
        print(max(array))


class DisplayArray(ArrayOperations):
    def do_something(self, array):
        print(array)


class DisplayMin(ArrayOperations):
    @staticmethod
    def do_something(self, array):
        print(min(array))


class DisplayReverse(ArrayOperations):
    @staticmethod
    def do_something(self, array):
        print(array[::-1])


class SaveFile(ArrayOperations):
    @staticmethod
    def do_something(self, array):
        with open(file='array.txt', mode='w', encoding='utf-8') as f:
            f.write(array)


array = [randint(1, 10) for _ in range(19)]

operation = ArrayOperations(DisplayMax)
operation.do_something(array)