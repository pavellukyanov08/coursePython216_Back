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
#     print('Список:', number)
#     count = 0
#     for i in number:
#         number.remove(int(input('Enter the number to delete: ')))
#         count += 1
#     print('Количество удаленных чисел:', count)
#
#     return number
#
#
# print(simp_number([randint(1, 50) for _ in range(10)]))
