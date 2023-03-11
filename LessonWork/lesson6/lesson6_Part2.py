import random

# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))
# row = [0] * n
# matrix = [row] * m
# for row in matrix:
#     print(*row)
# print(matrix[0][2])


# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))
# matrix = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
#
# for row in matrix:
#     for elm in row:
#         print(elm, end='\t')
#     print()


# heights = ['167', '175', '171', '180']
# heights = list(map(int, heights))
# print(heights)


# nums = list(map(int, input('Введите значения через пробел: ').split()))
#
# print(type(nums))
# print(nums)


# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))
# matrix = [[i for i in range(n)] for j in range(m)]
#
# for row in matrix:
#     for elm in row:
#         print(elm, end='\t')
#     print()


# matrix = []
# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))
# # matrix = [[i + n * j + 1 for i in range(n)] for j in range(m)]
# value = 1
#
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(value)
#         print(value, end='\t')
#         value += 1
#     print()
#     matrix.append(row)
# print('\t' * m)
#
# for i in range(m):
#     for j in range(n):
#         matrix[i][j] **= 2
#         print(matrix[i][j] **= 2
#     print()


# matrix = []
# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))
# # matrix = [[i + n * j + 1 for i in range(n)] for j in range(m)]
# value = 1
#
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(value)
#         print(value, end='\t')
#         value += 1
#     print()
#     matrix.append(row)
# print('\t' * m)
#
# for i in range(m):
#     for j in range(n):
#         matrix[i][j] **= 2
#         print(matrix[i][j] **= 2
#     print()


# wide = 10
# height = 10
# matrix = [[0 for i in range(10)] for j in range(10)]
# for i in range(10):
#     matrix[i][i] = 1
#     if i < len(matrix[0]) - 1:
#         matrix[i][i + 1] = 1
#     if i > 0:
#         matrix[i][i - 1] = 1
#
# for num in matrix:
#     for j in row:
#         print(num, end='\t')
#     print()



# matrix = [[random.randint(1, 10) for i in range(5)] for j in range(5)]

import random


