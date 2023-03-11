# Task 1
# def random_symb(a : int = 20, smb: str = '-'):
#     print(a * smb)
#
#
# random_symb()
# random_symb(30, #)


# Task 2
# def count_even_and_odd_numbers():
#     num = int(input('Число: '))
#     even, odd = 0, 0
#     for i in str(num):
#         if int(i) % 2 == 0:
#             even += int(i)
#         else:
#             odd += int(i)
#     print('sum of even numbers', even)
#     print('sum of odd numbers', odd)
#
#
# count_even_and_odd_numbers()

# def count_even_and_odd_numbers(num: int, even: bool = True):
#     list_nums = list(map(int, list(str(num))))
#     return sum([i for i in list_nums if i % 2 !=even])
#
#
# evens = 'не'
# print(f'Сумма четных: {count_even_and_odd_numbers(456465564646, not evens)}')


# Task 3
# def fibo(n: int):
#     if n == 1:
#         return 0
#     elif n == 2 or n == 3:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(10))

# def draw_symbol(length: int = 20, symbol: str = '-'):
#     if length > 0:
#         print(symbol, end='')
#         draw_symbol(length-1, symbol)
#
#
# draw_symbol(3, '*')


# Task 4
# def finding_degree():
#     num, deg = int(input('Введите число: ')), int(input('Введите степень: '))
#     return num * finding_degree(num, deg - 1) if deg > 0 else 1
#
# print(f'{num} в степени {deg} равно {power(num, deg)}')


# Task 5
# def count_summ(a, b):
#     return a + count_summ(a + 1, b) if a < b else b
#
#
# print(count_summ(6, 10))

# def count_summ(a: int, b: int) -> int:
#     return a + count_summ(a + 1, b) if a < b else b
#
#
# print(count_summ(a=int(input('число а: ')), b=int(input('число b: '))))
