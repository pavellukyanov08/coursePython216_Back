import math


#
# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     @staticmethod
#     def square_root(self):
#         return math.sqrt(self.num)
#
#     @staticmethod
#     def print(x):
#         print(x)
#
#
# a = Number(-5)
# a.square_root(12)


# Task 1
# class People:
#     count = 0
#
#     def __init__(self):
#         People.count += 1
#
#     @staticmethod
#     def get_count():
#         print(People.count)
#
#
# people1 = People()
#
# people1.get_count()


# Task 2
# class Area:
#     count = 0
#
#     @staticmethod
#     def count_triangle(a, b, p, c):
#         Area.count += 1
#         print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
#
#     @staticmethod
#     def count_triangle2(a, h):
#         Area.count += 1
#         print(a * h / 2)
#
#     @staticmethod
#     def count_rectangle(a, b):
#         Area.count += 1
#         print(a * b)
#
#     @staticmethod
#     def count_rhomb(d1, d2):
#         Area.count += 1
#         print(1 / 2 * d1 * d2)
#
#     @staticmethod
#     def count_square(a):
#         Area.count += 1
#         print(a * a)
#
#     @staticmethod
#     def get_count():
#         print(f'Кол-во подсчетов: {Area.count}')
#
#
# area1 = Area()
#
# area1.count_triangle(8, 9, 10, 6)
# area1.count_triangle2(9, 10)
#
# area1.count_rectangle(12, 10)
# area1.count_rhomb(14, 7)
# area1.count_square(5)
#
# area1.get_count()


# class Stadium:
#     def __init__(self, name, opening_date, country, city, capacity):
#         self.__name = name
#         self.__opening_date = opening_date
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     @property
#     def input_name(self):
#         return self.__name
#
#     @property
#     def input_opening_date(self):
#         return self.__opening_date
#
#     @input_name.setter
#     def input_name(self, name):
#         self.__name = name
#
#     @input_opening_date.setter
#     def input_opening_date(self, opening_date):
#         self.__opening_date = opening_date
#
#     def input_data(self):
#         # self.name(input('Введите название: '))
#         # self.opening_date(input('Введите дату открытия (дд.мм.гг): '))
#         self.country = (input('Введите страну: '))
#         self.city = (input('Введите город: '))
#         self.capacity = (int(input('Введите вместимость стадиона: ')))
#
#     def output_data(self):
#         print(f'\nНазвание: {self.name};\n дата открытия: {self.opening_date};\n страна: {self.country};\n '
#               f'город: {self.city};\n вместимость стадиона: {self.capacity}')
#
#
# stadium1 = Stadium('', '', '', '', '')
#
# stadium1.name = 'Арена славы'
# print(stadium1.name)
#
# stadium1.input_data()
# stadium1.output_data()


# Task 3
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def output_info(self):
#         print(f'Фигура: {self.name}')
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#
# shape = Shape('Фигура')
# shape.output_info()
# print(shape.output_info())
# print('-'*50)
#
# circle1 = Circle(5)
# circle1.output_info()
# print(circle1.output_info())
# print('-'*50)
#
# square1 = Square(4)
# square1.output_info()
# print(square1.output_info())
# print('-'*50)
