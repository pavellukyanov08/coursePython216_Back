# Task 1
from random import randint

# m, n = 5, 5
# matrix = [[randint(1, 10) for i in range(m)] for j in range(n)]
#
# summa = 0
#
# while len(matrix[0]):
#     maximum = []
#     for row in matrix:
#         local_max = max(row)
#         row.remove(local_max)
#         maximum.append(local_max)
#     summa += max(maximum)
#     print('--------------')
#     [print(*row, sep='\t') for row in matrix]
# print(summa)


# Task 2
# def get_perimeter(matrix):
#     perimeter = 0
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 1:
#                 if j == 0 or matrix[i][j] == 0:
#                     perimeter += 1
#                 elif j == len(matrix[0] - 1 or matrix[i][j + 1] == 0:
#                     perimeter += 1
#                 elif j == 0 or matrix[i - 1][j] == 0:
#                     perimeter += 1
#                 elif i == len(matrix) - 1 or matrix[i + 1][j] == 0:
#                     perimeter += 1
#     return perimeter


# print(get_perimeter([0, 0, 1, 0, 0],
#                     [0, 1, 1, 0, 0],
#                     0,))


# Task 3
# def shift(matrix, k=1):
#     m, n = len(matrix), len(matrix[0]))


# Крестики нолики
# board = [['#', '#', '#'],
#          ['#', '#', '#'],
#          ['#', '#', '#']]

# turn = 1


# def check_win(board, symbol):
#     if ((board[0][0] == board[0][1] == board[0][2] == symbol) or
#         (board[1][0] == board[1][1] == board[1][2] == symbol) or
#         (board[2][0] == board[2][1] == board[2][2] == symbol) or
#         (board[0][0] == board[1][0] == board[2][0] == symbol) or
#         (board[0][1] == board[1][1] == board[2][1] == symbol) or
#         (board[0][2] == board[1][2] == board[2][2] == symbol) or
#         (board[0][0] == board[1][1] == board[2][2] == symbol) or
#         (board[0][2] == board[1][1] == board[2][0] == symbol)):
#         return True
#     return False
#
#
# def make_turn(board, symbol):
#     while True:
#         try:
#             row = int(input('Введите номер ряда (1-3): '))
#             col = int(input('Введите номер столбца (1-3): '))
#             if ((row in [1, 2, 3] and col in [1, 2, 3]) and
#                board[row - 1][col - 1] == '#'):
#                 break
#             else:
#                 print('Ошибка! Неверный ввод.')
#         except ValueError:
#             pass
#     board[row - 1][col - 1] = symbol
#
#
# def tic_tac_toe(board, turn):
#     if turn > 9:
#         print('Ничья!')
#         return
#     symbol = 'X' if turn % 2 == 1 else 'O'
#     print(f'Ходят {symbol}. Ход: {turn}')
#     [print(*row, sep='\t') for row in board]
#     make_turn(board, symbol)
#     if check_win(board, symbol):
#         print(f'Победили {symbol}!')
#         [print(*row, sep='\t') for row in board]
#     else:
#         tic_tac_toe(board, turn + 1)
#
#
# tic_tac_toe(board, 1)


# def summa(a, b):
#     def check_ab(a, b):
#         return a > 0 and b > 0
#
#     if check_ab(a, b):
#         return a + b
#     return 'Wrong input'
#
#
# print(summa(2, -5))


# lambda - выражение
# add = lambda x: x + 1
# print(add(4))
#
#
# def add(x):
#     return x + 1
#
#
# print(add(4))


# lst = [(1, 2), (2, 2), (3, 3), (4, 4)]
# print(list(map(lambda x: x[0]**2 + x[1], lst)))


# lst = [[randint(1, 10) for _ in range(5)] for _ in range(4)]
# print(lst)
# lst.sort(key=sum, reverse=True)
# print(lst)


# lst = ['hello', 'append', 'asddsd', 'ddddd', 'weqwe']
#
# a_str = lambda string: [smb for smb in string if 'a' in smb]
# print('Четные числа: ', a_str(lst))
