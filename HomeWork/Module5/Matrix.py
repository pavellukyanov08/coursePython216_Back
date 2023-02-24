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


# Task 2
# w = int(input('Введите ширину матрицы: '))
# h = int(input('Введите высоту матрицы: '))
#
# a = [[0] * h for i in range(w)]
#
# for i in range(w):
#     for j in range(h):
#         a[i][j] = i + j
#
# for row in a:
#     print('\t'.join([str(elem) for elem in row]))


# Task 3
# import random
#
# matrix = []  # создаем пустой массив
# # Заполняем массив случайными числами (0-10)
# for i in range(5):
#     row = [random.randint(0, 10) for _ in range(5)]
#     matrix.append(row)
# # Выводим исходный массив
# print('Матрица 5х5:')
# for row in matrix:
#     for element in row:
#         print(element, end='\t')
#     print()
#
# # Находим столбец с минимальной суммой
# min_sum = float('inf')  # присваиваем бесконечное значение, т.к. min_sum > 0
# min_index = -1  # присваиваем -1, т.к. index > 0
# for col in range(len(matrix[0])):  # проходим по столбцам таблицы
#     sum_col = 0  # сумма значений текущего столбца
#     for row in range(len(matrix)):  # проходим по рядам таблицы
#         sum_col += matrix[row][col]  # добавляем значения текущего ряда в sum_col
#     if sum_col < min_sum:  # если sum_col < min_sum, то...
#         min_sum = sum_col  # ...задаем min_sum = sum_col...
#         min_index = col  # ...и min_index = col
#
# # Выводим результат
# print('\nРезультат:')
# for row in range(len(matrix)):  # проходим по рядам таблицы...
#     print(matrix[row][min_index])  # ...выводя элементы min_index-го столбца
