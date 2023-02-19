# Task 1
# from random import randint
#
#
# def simp_number(number):
#     # number = [randint(0, 100) for _ in range(10)]
#     print(f'Исходный список: {number}')
#
#     simple_numbers = []
#
#     for simple_number in number:
#         divider = 0
#         for j in range(1, simple_number + 1):
#             if simple_number % j == 0:
#                 divider += 1
#         if divider <= 2:
#             simple_numbers += [simple_number]
#
#     return simple_numbers  # простые числа
#
#
# print(simp_number([randint(0, 100) for _ in range(10)]))


# Task 2
# from random import randint
#
#
# def simp_number(number):
#     print('Список:', number)  # выводим исходный список
#     count = 0
#     num = int(input('Enter the number to delete: '))
#     for i in number[:-1]:   # перебираем числа списка
#         if i == num:    # если число в списке равно числу на удаление
#             number.remove(num)  # удаляем это число
#             count += 1  # увеличиваем счетчик
#
#     print('Количество удаленных чисел:', count)
#
#     return number
#
#
# print(simp_number([randint(1, 50) for _ in range(10)]))


# Task 4
# import math
# from math import sqrt, pi
#
#
# def calc_square():
#     figure = input('Введите фигуру (1 - треуг, 2 - прямоуг, 3 -  круг): ')
#     if figure == '1':
#         a = float(input("a = "))
#         b = float(input("b = "))
#         c = float(input("c = "))
#         p = (a + b + c) / 2
#         return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
#     elif figure == '2':
#         a = float(input("a = "))
#         b = float(input("b = "))
#         return a * b
#     elif figure == '3':
#         r = float(input('Радиус (r): '))
#         return round(r ** 2 * math.pi, 2)
#     else:
#         return 'Ошибка ввода'
#
#
# print(calc_square())
