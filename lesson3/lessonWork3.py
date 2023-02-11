# Task 1
# for i in range(1, 10):
#     for n in range(1, 10):
#         print(f"{n}*{i}={i * n}", end="\t")
#     print()


# Task 2
# m = int(input("укажите высоту: "))
# n = int(input("укажите ширину: "))
# s = input("Выберете символ: ")
#
# for i in range(m):
#     for j in range(n):
#         print(s, end="\t")
#     print()


# Task 3
# m = int(input("укажите высоту: "))
# n = int(input("укажите ширину: "))
# s = input("Укажите символ1: ")
# ss = input("Укажите символ2: ")
#
# for i in range(m):
#     for j in range(n):
#         if i % 2 == 0:
#             print(s, end="\t")
#         else:
#             print(ss, end="\t")
#     print()


# Task 4
# x = int(input("Введите первое число диапазона: "))
# y = int(input("Введите второе число диапазона: "))
# n = int(input("Введите число: "))
#
# while n < x or n > y:
#     print("Число вне диапазоне")
#     n = int(input("Введите число "))
#
# for i in range(x, y + 1):
#     num = i
#     if i == n:
#         num = '!' + str(i) + '!'
#     if i == y:
#         print(num)
#     else:
#         print(num, end=' ')


# Task 5
# num = int(input("Введите число: "))
# for i in range(1, num // 2 + 1 ):
#     if num % i == 0:
#         print(i, end='\t')


# Task 6
# import random
# import time
#
# attempt_number = 0
# start = time.time()
# number = random.randint(1, 500)
#
# while True:
#
#     attempt = int(input('Угадай число (от 1 до 500): '))
#
#     if attempt == 0:
#         print('Тебе надоело. Игра окончена =(')
#         break
#
#     elif attempt > number:
#         print('Число больше загаданного. Попробуй еще!')
#         attempt_number += 1
#
#     elif attempt < number:
#         print('Число меньше загаданного. Бери больше!')
#         attempt_number += 1
#
#     elif attempt == number:
#         end = time.time()
#         print(f'Ты угадал число, маладэц! Использовано {attempt_number} попыток!\nзатрачено времени: {end - start}')
#         break
#
#     else:
#         print(f'А вот и не угадал! Я загадал число {number}')


# Task 7
# row = 5
# space = ' '
# for i in range(row):
#     print(space * i + '*')


# Task 8
# string = ""
# for i in range(5+1):
#     string = string + str(i)
#     print(string)
