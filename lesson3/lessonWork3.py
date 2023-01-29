# import random
#
# for i in range(random.randint(0, 10)):
#     print(i)

# lnt = int(input('Введите длину: '))
# cnt = int(input('Введите количество: '))
#
# chr = input('Введите символ: ')
#
# for i in range(lnt):
#     for j in range(cnt):
#         print(chr, end='')
#     print()


# for i in range(5):
#     for j in range(10):
#         if (i+j) % 2 == 0:
#             print('+', end='\t')
#         else:
#             print('-', end='')
#     print()


# start = int(input('Первая страница: '))
# end = int(input('Вторая страница: '))
#
# while True:
#     num = int(input('Число: '))
#     if (num < start) and (num > end):
#         print('Число введено неправильно')
#         break
#
#     else:
#         for i in range(start, end + 1):
#             if i == num:
#                 print(f'!{i}!')
#             else:
#                 print(f'{i}', sep='')
#     continue


num = int(input('Число: '))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)










