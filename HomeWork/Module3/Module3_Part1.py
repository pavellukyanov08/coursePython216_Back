# Task 1
# num1 = int(input('Введите начала диапазона: '))
# num2 = int(input('Введите конец диапазона: '))
#
# for i in range(num1, num2 + 1):
#     if i % 7 == 0:
#         print(f'Числа кратные 7 из диапазона: {i}')


# Task 2
# num1 = int(input('Введите начало диапазона: '))
# num2 = int(input('Введите конец диапазона: '))
#
# numbers = [i for i in range(num1, num2 + 1)]
# print(f'Все числа диапазона: {numbers}')
# print(f'Числа в порядке убывания: {numbers[::-1]}')
#
# multiples_seven_numbers = []
# count_five = 0
# for i in range(num1, num2 + 1):
#     if i % 7 == 0:
#         multiples_seven_numbers.append(i)
#
#     if i % 5 == 0:
#         count_five += 1
#
# print(f'Числа кратные 7: {multiples_seven_numbers}')
# print(f'Количество чисел, кратных 5: {count_five}')


# Task 3
# num1 = int(input('Введите начало диапазона: '))
# num2 = int(input('Введите конец диапазона: '))
#
# for i in range(num1, num2 + 1):
#     if i % 3 and i % 5 == 0:
#         print('Fizz Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
