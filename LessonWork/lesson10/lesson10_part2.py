# Декораторы/decorators - функции, основной целью которых является
# изменение поведения других функций.


# def check_positive(func):
#     def wrapper(*args):
#         if func(*args) < 0:
#             return 'Error: sum is negative'
#         else:
#             return func(*args)
#     return wrapper
#
#
# @check_positive
# def summa(a, b, c):
#     return a + b + c
#
#
# print(summa(2, 3, 4))
# print(summa(2, -3, -1))


# def prettify_output(func):
#     def wrapper(*args):
#         print('**********')
#         func(*args)
#         print('**********')
#     return wrapper
#
#
# @prettify_output
# def print_hello(a, b, c, f, s, g):
#     print('Hello World!')
#
#
# print_hello(1, 2, 2, 2, 2, 2)


# def print_stars(func):
#     print('*' * 10)
#     func()
#
#
# @print_stars
# def print_hello(name):
#     print(f'Hello {name}!')


# Неограниченное количество позиционных аргументов и аргументов по ключу
# def summa(*args, **kwargs):
#     print(args, kwargs)
#     return sum(args) + sum(kwargs.values())
#
#
# print(summa(5, 2, 2, 2, 2, 2, 2, 2))
# print(summa(5, 2, 2, 2, 2, 2, 2, 2, a=2))
# print(5, 2, 4, **{'sep': '==', 'end': 'BLABLABLA'})


# 1. Напишите декоратор logging, который будет вести
# логи вызова функции. В них он должен будет отображать
# аргументы и результат вызова функции.
# Пример:
# @logging
# def summa(a, b):
#     return a + b
#
# >>> summa(2, 3)
# Function summa was called with arguments: 2, 3 and returned 5
# Подсказка: Имя функции - это func.__name__
# print(print.__name__) -> 'print'

# def logging(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Function {func.__name__} was called with arguments: {*args, kwargs} and returned {result}')
#         return result
#     return wrapper
#
#
# @logging
# def summa(a, b, c, d):
#     return a + b - c - d
#
#
# print(summa(2, 3, c=2, d=5))


# 2.

# Напишите декоратор, который измеряет время,
# необходимое для выполнения функции, и
# печатает время выполнения.


# def timer(func):
#     def wrapper(*args, **kwargs):
#         from time import time
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(f'Function {func.__name__} runned in {end - start} seconds')
#         return result
#     return wrapper
#
#
# @timer
# def create_random_list():
#     import random
#     return [random.randint(-100000, 100000) for i in range(1000000)]
#
#
# create_random_list()


# 3.

# Напишите декоратор, кэширующий результаты
# функции, чтобы при повторной передаче
# функции тех же входных данных кэшированные
# результаты возвращались вместо их
# повторного вычисления.


# def caching(func):
#     cache = {}
#
#     def wrapper(*args, **kwargs):
#         if (args, *kwargs.items()) not in cache:
#             cache[(args, *kwargs.items())] = func(*args, **kwargs)
#         return cache[(args, *kwargs.items())]
#     return wrapper
#
#
# @caching
# def cached_fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return cached_fibo(n - 1) + cached_fibo(n - 2)
#
#
# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(cached_fibo(50))


# Создание декоратора с параметром
# import random
#
#
# def retry(num):
#     def decorator(func):
#         count = 0
#
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             while count < num:
#                 try:
#                     return func(*args, **kwargs)
#                 except ValueError:
#                     count += 1
#                     print('Function failed')
#             raise Exception('Too many calls!')
#         return wrapper
#     return decorator
#
#
# @retry(3)
# def random_func():
#     if random.randint(0, 1):
#         raise ValueError
#     return 'Function successfully executed'
#
#
# @retry(2)
# def random_func2():
#     if random.randint(0, 5):
#         raise ValueError
#     return 'Function successfully executed'