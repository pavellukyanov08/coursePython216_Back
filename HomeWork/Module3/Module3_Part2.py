# Task 1
# from statistics import mean
#
# num1 = int(input('Введите 1 число: '))
# num2 = int(input('Введите 2 число: '))
#
# sum_even_numbers = 0
# sum_odd_number = 0
# sum_nine_number = 0
#
# even_numbers_list = []
# odd_numbers_list = []
# nine_list = []
#
# for i in range(num1, num2 + 1):
#     if i % 2 == 0:
#         sum_even_numbers += i
#         even_numbers_list.append(i)
#     if i % 2 != 0:
#         sum_odd_number += i
#         odd_numbers_list.append(i)
#     if i % 9 == 0:
#         sum_nine_number += i
#         nine_list.append(i)
#
# print(f'Сумма четных чисел: {sum_even_numbers}, среднее арифметическое: {mean(even_numbers_list)}')
# print(f'Сумма нечетных чисел: {sum_odd_number}, среднее арифметическое: {mean(odd_numbers_list)}')
# print(f'Сумма чисел кратных 9: {sum_nine_number}, среднее арифметическое: {mean(nine_list)}')


# Task 2
# lnt = int(input('Введите длину линии: '))
# smb = input('Введите символ: ')
#
# for i in range(lnt):
#     print(smb)


# Task 3
# while True:
#     num = int(input('Введите число: '))
#     if num > 0:
#         print('Number is positive')
#     elif num < 0:
#         print('Number is negative')
#     else:
#         print('Number is equal to zero')
#     if num == 7:
#         print('Good bye!')
#         break


# Task 4
# nums_list = []
#
# while True:
#     nums = int(input('Введите число: '))
#
#     nums_list.append(nums)
#
#     print(f'Сумма чисел: {sum(nums_list)}')
#     print(f'Сумма чисел: {max(nums_list)}')
#     print(f'Сумма чисел: {min(nums_list)}')
#
#     if nums == 7:
#         print('Good bye!')
#         break
