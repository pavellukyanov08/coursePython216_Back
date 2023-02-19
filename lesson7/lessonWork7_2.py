# import random
# random.seed(2)
#
# print(random.randint(1, 4))
# # print(random.random())
import random


def get_min_main_diag(matrix):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                lst.append(matrix[i][j])
    return min(lst)

n = int(input('Размер матрицы: '))
matrix = [random.randint(1, 100) for i in range(n) for j in range(n)]
for row in matrix:
    for el in row:
        print(el, end='\t')
    print()
print(get_min_main_diag())