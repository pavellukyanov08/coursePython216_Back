#Task1
# num = int(input('Enter a number: '))
#
# if num >= 1 or num > 100:
#     if num % 3 == 0 and num % 5 == 0:
#         print('Fizz Buzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)
#
# else:
#     print('Что-то пошло не так =(')




#Task2
# import math
#
# number = int(input("Enter number: "))
# degree = int(input("Enter degree: "))
#
# if 0 <= degree <= 7:
#     # метод возведения в степень (1 знач. – число, 2 - степень)
#     print(math.pow(number, degree))
# else:

#     print("Неверная степень")




#Task3
# time_call = int(input('Enter the time of call (seconds): '))
#
# operator = input('Choose the opertor mts (mts), beeline (b), megafon (m): ')
#
# mts = 100; beeline = 200; megafon = 300
#
# if operator == 'mts':
#     print(f'Стоимость звонка mts: {time_call * mts}')
# elif operator == 'b':
#     print(f'Стоимость звонока beeline: {time_call * beeline}')
# elif operator == 'm':
#     print(f'Стоимость звонка megafon {time_call * megafon}')
#
#
#
#
# #Task4
# managers = [int(input('Enter the sale amount for manager ' + str(i + 1))) for i in range(3)]
#
# for i in range((len(managers))):
#     if managers[i]<= 500:
#         print(f'Зарплата первого составляет: {200 + managers[i] * 0.3} долларов')
#     elif managers[i] <= 1000:
#         print(f'Зарплата составляет: {200 + managers[i] * 0.5} долларов')
#     else:
#         print(f'Зарплата составляет: {200 + managers[i] * 0.8} долларов')
#
# print("Лучшая зарплата: \033[32m{}".format(max(managers) + 200))