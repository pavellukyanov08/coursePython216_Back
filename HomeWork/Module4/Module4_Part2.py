# Task 1
# num = input('Введите арифметическое выражение (+, -, *, /): ')
#
# if '+' in num:
#     a, b = num.split('+')
#     print(f'Сложение: {int(a) + int(b)}')
# elif '-' in num:
#     a, b = num.split('-')
#     print(f'Вычитание: {int(a) - int(b)}')
# elif '*' in num:
#     a, b = num.split('*')
#     print(f'Умножение: {int(a) * int(b)}')
# elif '/' in num:
#     try:
#         a, b = num.split('/')
#         print(f'Деление: {int(a) / int(b)}')
#
#     except ZeroDivisionError:
#         print('Деление на ноль!')
#
# else:
#     print('Неверная операция')


# Task 2
# import random
#
# counter_negative = 0
# counter_zero = 0
#
# random_number = [random.randint(-50, 50) for i in range(100)]
# print(random_number)
#
# for num in random_number:
#     if num < 0:
#         counter_negative += 1
#     elif num == 0:
#         counter_zero += 1
#
# print(f'Минимальный: {min(random_number)}')
# print(f'Минимальный: {max(random_number)}')
#
# print(f'Количество отрицательных: {counter_negative}')
# print(f'Количество нулей: {counter_zero}')
