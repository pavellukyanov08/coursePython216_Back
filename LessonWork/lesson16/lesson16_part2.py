# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     def __int__(self):
#         return int(self.area)
#
#     def __str__(self):
#         info = ''
#         info += f'{self.__class__.__name__}:\n'
#         for key, value in self.__dict__.items():
#             info += f'\t{key}: {value}\n'
#         return info
#
#
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def area(self):
#         return self.r**2 * math.pi
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def area(self):
#         return self.a * self.b
#
#
# class RightTriangle(Shape):
#     def __init__(self, kat1, kat2):
#         self.kat1 = kat1
#         self.kat2 = kat2
#
#     @property
#     def area(self):
#         return self.kat1 * self.kat2 * 0.5
#
#
# class Trapezoid(Shape):
#     def __init__(self, base1, base2, h):
#         self.base1 = base1
#         self.base2 = base2
#         self.h = h
#
#     @property
#     def area(self):
#         return (self.base1 + self.base2) / 2 * self.h
#
#
# a = Circle(5)
# b = Rectangle(2, 3)
# c = RightTriangle(3, 4)
# d = Trapezoid(10, 6, 3)
# shapes = [a, b, c, d]
# for shape in shapes:
#     print(shape.area)
#     print(int(shape))
#     print(shape)


# 3.

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        info = ''
        info += f'{self.__class__.__name__}:\n'
        for key, value in self.__dict__.items():
            info += f'\t{key}: {value}\n'
        return info

    def save(self, filename='file.txt'):
        try:
            Shape.load(filename)
        except Exception:
            open(filename, 'w')
        with open(filename, 'a') as f:
            f.write(f'{self.__class__.__name__}(**{self.__dict__})\n')

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            if len(lines) == 1:
                return eval(lines[0])
            else:
                return list(map(eval, lines))

    def __str__(self):
        return self.show()


class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        Shape.__init__(self, x, y)
        self.a = a
        self.b = b


class Square(Shape):
    def __init__(self, x, y, a):
        Shape.__init__(self, x, y)
        self.a = a


class Ellipse(Rectangle):
    pass
#
#
# shapes = [Circle(10, 10, 5), Square(20, 20, 10),
#           Rectangle(30, 30, 5, 7), Ellipse(40, 40, 7, 5)]
#
# for shape in shapes:
#     shape.save('file.txt')
#
# new_shapes = Shape.load('file.txt')
# for shape in new_shapes:
#     print(shape)


# import pickle
#
# string = Circle(2, 3, 5)
# with open('file.txt', 'wb') as f:
#     pickle.dump(string, f)
#
# with open('file.txt', 'rb') as f:
#     text = pickle.load(f)
#     print(text)

# pickle.dumps()
# pickle.loads()


# import json
#
# circles = []
# for i in range(1, 10):
#     obj = Circle(i, 3, 5)
#     circles.append(f'{obj.__class__.__name__}(**{obj.__dict__})')
#
# with open('file.txt', 'w') as f:
#     json.dump(circles, f)
# with open('file.txt', 'r') as f:
#     text = json.load(f)
#     # obj_eval = f'{list(text.keys())[0]}(**{list(text.values())[0]})'
#     # print(eval(obj_eval))
#     # new_obj = locals()[text[0]]
#     # kwargs = list(text.values())[0]
#     # print(new_obj(**kwargs))
#     for obj in text:
#         print(eval(obj))


# import csv
#
# file = csv.reader(open('file.csv', 'r'))
# for i in file:
#     print(i)
#
# writer = csv.writer(open('file.csv', 'a'))
# writer.writerow([7, 6, 5, 4])


# import json
#
#
# def add_country(country, capital, countries):
#     if no_country(country, countries):
#         countries[country] = capital
#     else:
#         print('That country is already added')
#
#
# def no_country(country, countries):
#     if country not in countries:
#         return 'There are no country in dict that you provided'
#     return False
#
#
# def reset_capital(country, capital, countries):
#     def set_capital():
#         countries[country] = capital
#         return countries[country]
#     print(no_country(country, countries) or set_capital())
#
#
# def delete_country(country, countries):
#     print(no_country(country, countries) or countries.pop(country))
#
#
# def find_capital(country, countries):
#     print(no_country(country, countries) or countries[country])
#
#
# def save_countries(countries):
#     with open('countries.txt', 'w') as f:
#         json.dump(countries, f)
#
#
# def load_countries():
#     with open('countries.txt', 'r') as f:
#         countries = json.load(f)
#         return countries
#
#
# def main():
#     countries = load_countries()
#     command = ''
#     while command != 'exit':
#         print(f'1. Добавить страну\n'
#               f'2. Изменить столицу у страны\n'
#               f'3. Найти столицу по стране\n'
#               f'4. Удалить страну\n'
#               f'5. Загрузить страны из файла\n'
#               f'6. Сохранить страны в файл\n'
#               f'7. Показать все страны и их столицы\n'
#               f'exit. Выход')
#         command = input('Введите команду для исполнения: ')
#         if command == '1':
#             add_country(input('Введите страну: ').capitalize(),
#                         input('Введите столицу: ').capitalize(),
#                         countries)
#         elif command == '2':
#             reset_capital(input('Введите страну: ').capitalize(),
#                           input('Введите столицу: ').capitalize(),
#                           countries)
#         elif command == '3':
#             find_capital(input('Введите страну: ').capitalize(),
#                          countries)
#         elif command == '4':
#             delete_country(input('Введите страну: ').capitalize(),
#                            countries)
#         elif command == '5':
#             save_countries(countries)
#         elif command == '6':
#             countries = load_countries()
#         elif command == '7':
#             for key, value in countries.items():
#                 print(f'{key}: {value}')
#         elif command == 'exit':
#             break
#         else:
#             print('There is no command like this!!!')
#
#
# if __name__ == '__main__':
#     main()
