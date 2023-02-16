# Task 1

# from random import randint
#
# W = 10
# H = 10
#
# count = []
# matrix = []
#
# for i in range(W):
#     row = []
#     # Строка заполняется элементами
#     for j in range(H):
#         n = int(randint(10, 1000))
#         if 99 < n < 1000:
#             count += [n]
#         row.append(n)
#     matrix.append(row)
# # Вывод матрицы на экран.
# # На каждой итерации внешнего цикла переменной i присваивается целая строка матрицы.
# for i in matrix:
#     # Во внутреннем цикле извлекается каждый отдельный элемент строки
#     for j in i:
#         print(j, end='\t')
#     print()
# print('Three-digit number:', count)
#
# multiplay_five = []
# for n in count:
#     print('Number:', n)
#     summ = 0
#     while n > 0:
#         digit = n % 10
#         summ += digit
#         n = n // 10
#     if summ % 5 == 0:
#         multiplay_five.append(summ)
#     print('Sum:', summ)
# print('Sum is multiplay 5:', multiplay_five)
