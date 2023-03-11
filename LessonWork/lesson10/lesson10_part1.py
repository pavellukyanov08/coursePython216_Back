# 1.
# a, b, c = (0, 4, 1, 5, 2), (6, 2, 5, 7, 8), (8, 1, 0, 2, 5)
#
# [print(num) for num in a if num in b and num in c]

# 2.

# a, b, c = (0, 4, 1, 5, 2), (6, 2, 5, 7, 8), (8, 1, 3, 2, 5)
#
# [print(num) for num in a if num not in b and num not in c]
# [print(num) for num in b if num not in b and num not in c]
# [print(num) for num in c if num not in b and num not in c]


# 6.

# country_to_capital = {}
# while True:
#     command = input('1. add\n'
#                     '2. delete\n'
#                     '3. find\n'
#                     '4. replace\n'
#                     'Введите команду: ')
#     if command == '1' or command == 'add':
#         country = input('Введите страну: ')
#         capital = input('Введите столицу: ')
#         country_to_capital[country] = capital
#     elif command == '2' or command == 'delete':
#         country = input('Введите страну: ')
#         del country_to_capital[country]
#     elif command == '3' or command == 'find':
#         choice = input('Введите 1, если хотите найти одну столицу\n'
#                        'Или 2, если хотите найти все страны и столицы '
#                        'по вашему слову: ')
#         if choice == '1':
#             country = input('Введите страну: ')
#             print(f'Столица страны {country} - {country_to_capital[country]}')
#         else:
#             part_name = input('Введите часть названия страны: ')
#             [print(f'Страна: {country}, Столица: {capital}')
#              for country, capital in country_to_capital.items() if
#              country.startswith(part_name.lower().capitalize())]
#     elif command == '4' or command == 'replace':
#         country = input('Введите страну: ')
#         capital = input('Введите новую столицу: ')
#         country_to_capital[country] = capital


# Замыкания - closure(с ан. яз)

# def outer(par):
#     loc = par
#     def inner():
#         return loc
#     return inner
#
# var = 1
# fun = outer(var)
# print(fun())


# def makeclosure(par):
#
#     def power(p):
#         return p ** par
#     return power
#
#
# func_sqr = makeclosure(3)
# print(func_sqr(3))


# 1.
# Напишите функцию, которая создаёт другую функцию.
# Эта созданная функция должна изменять вывод данных
# в зависимости от символа, который был передан в первую
# функцию.

# Пример:
# pretty_stars = func('*')
#
# pretty_stars('Name')
# >>> '*Name*'

# def make_pretty_func(symbol):
#
#     def pretty(string):
#         return symbol + string + symbol
#
#     return pretty
#
# pretty_stars = make_pretty_func('*')
# pretty_dollars = make_pretty_func('$')
# print(pretty_stars('Егор'))
# print(pretty_dollars('Максим'))


# ------------------Пространства имен-----------------
# n = 10
# def new():
#     n = 5
#     def create():
#         global n
#         num = n
#         nonlocal n
#         print(num + n)
#     create()
#
# new()


# 2.
# Напишите функцию счетчик, которая возвращает
# замыкание, отслеживающее, сколько раз оно
# было вызвано. Замыкание не должно принимать
# аргументов и возвращать целое число,
# представляющее количество раз, когда оно
# было вызвано.

# Пример использования:
# >>> c = counter()
# >>> c()
# 1
# >>> c()
# 2
# >>> c()
# 3

# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     return inner
#
# c = counter()
# c()
# c()
# c()


# 3.
# Напишите функцию нахождения среднего,
# которая возвращает замыкание.
# Замыкание должно принимать один аргумент,
# представляющий число в последовательности,
# и возвращать текущее среднее значение.

# Пример использования:
# >>> avg = average()
# >>> avg(10)
# 10.0
# >>> avg(20)
# 15.0
# >>> avg(30)
# 20.0

# def average():
#     count = 0
#     total = 0
#
#     def inner(num):
#         nonlocal count, total
#         count += 1
#         total += num
#         return total/count
#     return inner
#
#
# avg = average()
# print(avg(10))
# print(avg(5))
# print(avg(0))


# 4.
# Напишите функцию password_protected, которая
# принимает пароль в качестве аргумента и
# возвращает замыкание, которое можно
# использовать для защиты доступа к
# конфиденциальной функции. Закрытие должно
# принимать один аргумент, представляющий
# пароль,
# и возвращать результат чувствительной
# функции, если пароль правильный,
# и сообщение об ошибке в противном случае.

# Пример использования:
# >>> def sensitive_function():
# ...     return "You have accessed a sensitive function!"
# ...
# >>> protected_function = password_protected("abc123")
# >>> protected_function("abc123")
# "You have accessed a sensitive function!"
# >>> protected_function("incorrect_password")
# "Error: incorrect password"

# def sensitive_function():
#     return "You have accessed a sensitive function!"
#
#
# def password_protected(password):
#     def inner(pw):
#         if pw == password:
#             return sensitive_function()
#         else:
#             return "Error: incorrect password"
#     return inner
#
#
# protected_function = password_protected("abc123")
# print(protected_function("abc123"))
# print(protected_function("321"))
# print(protected_function("abc123"))


# 5.

# Напишите функцию memoize, которая принимает
# функцию в качестве аргумента и возвращает
# замыкание, кэширующее результаты функции.
# Замыкание должно принимать любое количество
# аргументов и возвращать кэшированный
# результат, если те же аргументы были
# переданы ранее, или вычислять и кэшировать
# результат в противном случае.

# Пример использования:

# >>> def slow_add(x, y):
# ...     print("Computing...")
# ...     return x + y
# ...
# >>> fast_add = memoize(slow_add)
# >>> fast_add(1, 2)
# Computing...
# 3
# >>> fast_add(1, 2)
# 3
# >>> fast_add(2, 3)
# Computing...
# 5


# def memoize(f):
#     cache = {}
#
#     def inner(*args):
#         if args not in cache:
#             cache[args] = f(*args)
#         return cache[args]
#     return inner
#
#
# def slow_add(x, y):
#     print("Computing...")
#     return x + y
#
#
# fast_add = memoize(slow_add)
# print(fast_add(1, 2))
# print('------------')
# print(fast_add(1, 2))
# print('------------')
# print(fast_add(2, 3))
# print('------------')
# print(fast_add(2, 3))
