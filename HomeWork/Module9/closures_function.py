# Task 1
# def repeat_until(f, p):
#     def closure(x):
#         while not p(x):
#             x = f(x)
#         return x
#     return closure
#
#
# def half(x):
#     return x // 2
#
#
# def is_even(x):
#     return x < 5
#
#
# increment_until_5 = repeat_until(half, is_even)
#
# print(increment_until_5(19))


# Task 2
# 1.
# def counter(n):
#     def inner():
#         nonlocal n
#         for i in range(n, 0, -1):
#             print(i)
#     return inner
#
#
# c = counter(5)
# c()


# 2.
# def make_counter(n):
#     def counter():
#         nonlocal n
#         if n > 0:
#             n -= 1
#             print(n)
#     return counter
#
#
# c = make_counter(5)
# c()
# c()
# c()
# c()
# c()


# Task 3
# def once_called(func):
#     already_called = False
#
#     def inner(*args):
#         nonlocal already_called
#         if not already_called:
#             func(*args)
#             already_called = True
#     return inner
#
#
# def my_func():
#     print('Hello world')
#
#
# once = once_called(my_func)
#
# once()
# once()
# once()
