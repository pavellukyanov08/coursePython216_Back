# try:
#     apples = int(input('Enter quantity of apples: '))
#     peoples = int(input('Enter quantity of peoples: '))
#     if apples < 0 or peoples < 0:
#         raise Exception
#     if apples > 20:
#         raise KeyError
#     print(f'Everyone should get {apples / peoples} apples')
#

# except ValueError:
#     print('Entered incorrect value')
#
# except ZeroDivisionError:
#     print('Division by zero')
#
# except Exception as ex:
#     print('You cant use negative numbers')
#
# finally:
#     print('Program is end')


# first = int(input('Enter first number: '))
# last = int(input('Enter last number: '))
#
# counter = first
#
# while counter <= last:
#     if counter % 2 != 0:
#         print(counter)
#     counter += 1

# first = int(input('Enter first number: '))
# last = int(input('Enter last number: '))
#
# counter = first
#
# if first > last:
#     first, last = last, first
#
# while counter <= last:
#     if counter % 2 != 0:
#         print(counter)
#     counter += 1


# a = int(input())
# b = int(input())
#
# i = max([a, b])
# while a <= i:
#     if a % 2 == 1:
#         print(a)
#     a += 1


# start, end = int(input('Введите первое число: ')), int(input('Введите второе число: '))
# if start > end:
#     start, end = end, start
# while start <= end:
#     if start % 2 != 0:
#         print(start)
#     start += 1


# a = int(input('1: '))
# b = int(input('2: '))
#
# sum = 0
# counter = 0
#
# while a <= b:
#     sum += a
#     counter += 1
#     a += 1
# print(sum)
# print(sum / counter)


# a, b = input('1: '), input('2: ')
# try:
#     print(f'Сумма: {int(a) + int(b)}')
# except ValueError:
#     print(f'Строка: {str(a) + str(b)}')


# num = int(input('Длина: '))
# symb = input('Символ: ')
#
# line = ''
# while num > 0:
#     print(symb, end='')
#     num -= 1


# res = 1
# while True:
#     a = int(input('Число: '))
#     if a == 0:
#         break
#     res *= a
# print(res)
