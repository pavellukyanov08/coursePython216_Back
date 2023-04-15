from abc import ABC, abstractmethod


#
#
# class A(ABC):
#     def __init__(self, size):
#         self.size = self.set_size(size)
#
#     def set_size(self, size):
#         return size
#
#     @abstractmethod
#     def get_size(self):
#         pass
#
#
# class B(A):
#     def __init__(self, size):
#         A.__init__(self, size)
#         self.other = 5
#
#     def get_size(self):
#         return self.size
#
#
# b = B(6)
# print(b.size)
# print(b.get_size())


# Task 1
# class Human(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'Это {self.name}. Возраст: {self.age}'
#
#     @abstractmethod
#     def occupation(self):
#         pass
#
#
# class Builder(Human):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def build_building(self, name):
#         print(f'Название здания: {name}')
#
#     def date_construction(self, date):
#         print(f'Дата постройки: {date}')
#
#
# class Sailor(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def sailing_time(self, time):
#         print(f'Время плавания: {time}')
#
#     def sailing_time(self, fish):
#         print(f'Кол-во пойманной рыбы: {fish}')
#
#
# hum = Sailor('John')
# hum.get_name()
# hum.get_age()


# class Time:
#     def __init__(self, hours, mins, secs):
#         self.hours = hours
#         self.mins = mins
#         self.secs = secs
#
#     def __add__(self, other):
#         return Time(self.hours + other.hours,
#                     self.mins + other.mins,
#                     self.secs + other.secs)
#
#
# a = Time(12, 0, 0)
# b = Time(14, 30, 0)
#
# c = a + b
# print(c.hours, c.mins)


# Task 2
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Number(self.value + other.value)
#
#     def __sub__(self, other):
#         return Number(self.value - other.value)
#
#     def __mul__(self, other):
#         return Number(self.value * other.value)
#
#     def __truediv__(self, other):
#         return Number(self.value / other.value)
#
#
# a = Number(5)
# b = Number(20)
#
# c = a + b
# print(c.value)
#
# c = a - b
# print(c.value)
#
# c = a * b
# print(c.value)
#
# c = a / b
# print(c.value)


# Task 3
class Library:
    def __init__(self, name, address, book_num):
        self.name = name
        self.address = address
        self.book_num = book_num

    def __add__(self, value):
        self.book_num + value

    def __iadd__(self, value):
        self.book_num += value

    def __sub__(self, value):
        self.book_num -= value

    def __str__(self):
        return f"Библиотека (name='{self.name}', адрес='{self.address}', количество книг={self.num_books})"

