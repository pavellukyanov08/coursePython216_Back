#Task 1
# for i in range(1, 10):
#     for n in range(1, 10):
#         print(f"{n}*{i}={i * n}", end="\t")
#     print()
#Task 2
# m = int(input("укажите высоту: "))
# n = int(input("укажите ширину: "))
# s = input("Выберете символ: ")
#
# for i in range(m):
#     for j in range(n):
#         print(s, end="\t")
#     print()

#Task 3

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

#Task 4
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

#Task 5

# num = int(input("Введите число: "))
# for i in range(1, num // 2 + 1 ):
#     if num % i == 0:
#         print(i, end='\t')

#Task 6
# import time
# import random
# # число попыток угадать
# guesses_made = 0
# # получаем имя пользователя из консольного ввода
# name = input('Привет! Как тебя зовут?\n')
# start = time.time()
# # получаем случайное число в диапазоне от 1 до 500
# number = random.randint(1, 500)
# print(f'Отлично, {0}, я загадал число между 1 и 500. Сможешь угадать?'.format(name))
# # пока пользователь не превысил число разрешенных попыток - 6
# while guesses_made < 5:
#     # получаем число от пользователя
#     guess = int(input('Введи число: '))
#     # увеличиваем счетчик числа попыток
#     guesses_made += 1
#     if guess < number:
#         print('Твое число меньше того, что я загадал.')
#     if guess > number:
#         print('Твое число больше загаданного мной.')
#     if guess == number:
#         break
# if guess == number:
#     print(f'Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
# else:
#     print(f'А вот и не угадал! Я загадал число {0}'.format(number))
# end = time.time()
# print(f'{name} потратил - {end - start} секунд')

#Task 7
# row = 5
# space = ' '
# for i in range(row):
#     print(space * i + '*')

#Task 8
# string = ""
# for i in range(5+1):
#     string = string + str(i)
#     print(string)
