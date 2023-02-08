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