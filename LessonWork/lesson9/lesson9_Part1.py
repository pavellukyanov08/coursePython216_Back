from random import randint

#
#
# def bulls_and_cows(number=str(randint(1000, 9999)), turn=1):
#     guess = input(f'Ход {turn}. Введите вашу догадку: ')
#     cows, bulls = 0, 0
#     num_copy = number[:]
#     for i in range(3, -1, -1):
#         if number[i] == guess[i]:
#             cows += 1
#             num_copy = num_copy[:i] + num_copy[i + 1:]
#             guess = guess[:i] + guess[i+1:]
#
#     for i in range(len(guess)-1, -1, -1):
#         if guess[i] in num_copy:
#             bulls += 1
#             index = num_copy.find(guess[i])
#             num_copy = num_copy[:i] + num_copy[i + 1]
#     print(cows, bulls)
#     if cows == 4:
#         print(f'Ты победил! Я загадал {number}. Кол-во ходов: {turn}')
#     else:
#         bulls_and_cows(number, turn + 1)
#
#
# bulls_and_cows()


# Тесты
# import time
# import sys
# size = 100000000
# my_tuple = tuple(range(size))
# my_list = list(range(size))
#
# print(sys.getsizeof(my_tuple), sys.getsizeof(my_list))


# Task 1
# my_tuple = ('apple', 'banana', 'mango', 'apple', 'mango')
# print(my_tuple.count(input('enter the fruit: ')))


# Task 2
# fruit_tuple = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
#
# counter = 0
# for i in fruit_tuple:
#     if 'banana' in i:
#         counter += 1
#
# print('Кол-во фрукта', counter)


# Task 3
# cars_tuple = ('Volkswagen', 'BMW', 'Mercedes', 'Honda', 'Subaru')
#
# car_name, replace_car = input('Введите марку: '), input('Введите замену: ')
# print(tuple(replace_car if brand == car_name else brand for brand in cars_tuple))


# countries = {'USA', 'Netherland', 'Norway', 'UK'}
#
# while True:
#     match command := input('Введите ваш запрос\n'
#                            '1 - Добавить страну\n'
#                            '2 - Удалить страну\n'
#                            '3 - Найти страну по первым символам\n'
#                            '4 - Найти страну по наименованию\n'
#                            '0 - Выход\n: '):
#
#         case '1':
#             countries.add(input('Добавить страну: '))
#             print(countries)
#
#         case '2':
#             countries.discard(input('Удалить страну: '))
#             print(countries)
#
#         case '3':
#             symbol = input('Введите символ: ')
#             for i in countries:
#                 if symbol in i:
#                     print(i)
#
#         case '4':
#             print(countries.isdisjoint(input('Проверить есть страна: ')))
#
#         case '0':
#             break
#
# print('Программа остановлена')
