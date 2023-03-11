# people = ['Egor', 'Sasha', 'Vadim', 'Lena', 'Diana']
# heights = [180, 190, 175, 178, 184]
# data = [[heights[i], i] for i in range(5)]
# data.sort(reverse=True)
# for i in range(5):
#     for j in range(i, 1 + 5):
#         if data[i][0] < data[j][0]:
#             data[i], data[j] = data[j], data[i]
# print(data)
# sorted_people = [people[value[1]] for value in data]
# print(sorted_people)



# def summ(a, b):
#     print(f'Сумма через print: {a + b}')
#     return a * b
#
#
# summ(10, 10)
#
# res = summ(10, 20)
# print(res)


# def multiplay(a: int, b: int):
#     return a * b
#
#
# print(multiplay(2, 2))
# print(multiplay(3, 2))
# print(multiplay(5, 2))

# print(range(5))
# print(range(1, 5))
# print(range(2, 5, 4))


# def lucky_number(n):
#     return n % 10 + n // 10 % 10 + n // 100 % 10 == n // 1000 % 10 + n // 10000 % 10 + n // 100000
#
#
# print(lucky_number(int(input('Введите число: '))))


# def is_lucky(num):
#     num = str(num)
#     return int(num[0]) + int(num[1]) + int(num[2]) == \
#         int(num[0]) + int(num[1]) + int(num[2])
#
#
# print(is_lucky(123420))

from random import randint
# def sort_matrix(matrix):
#     for i in range(len(matrix)):
#         if i % 2 == 0:
#             matrix[i].sort()
#         else: matrix[i].sort(reverse=True)
#         return matrix
#
#
# print(sort_matrix())


# def sort_matrix(matrix):
#     even = 0
#     for row in matrix:
#         row.sort(reverse=even % 2)
#         even += 1
#     return [matrix[i].sort(reverse=i % 2) for i in range(len(matrix))]
#
#
# matrix = [[random.randint(1, 10) for i in range(5)] for j in range(5)]
#
# print(matrix)
#
# sort_matrix(matrix)
#
# print(matrix)


# def random_matrix_product():
#     length = randint(3, 5)
#     matrix = [[randint(0, 4) for i in range(length) for j in range(randint(3, 5))]]
#
#     result = 1
#     for row in matrix:
#         for el in row:
#             result *= el if el > 0 else result
#             print(el, end='\t')
#         print()
#     return result


# print(random_matrix_product())