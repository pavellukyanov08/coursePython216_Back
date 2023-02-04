# Task 1
# rows = int(input("Введите количество строк: "))
#
# figure = input("Выберите фигуру \"Смотрите инстуркцию\"  ")
#
# if figure == "a":
#     print(*[((rows + 1) - i) * ' ' + i * '*' for i in range(rows, 0, -1)], sep='\n')
#
# elif figure == "b":
#     s, m = "*", []
#     for i in range(rows):
#         m = []
#         for k in range(i + 1):
#             m += s
#         print(*m)
#
# elif figure == "v":
#     for i in range(rows, 0, -1):
#         print((rows - i) * ' ' + i * '* ')
#
# elif figure == "g":
#     for i in range(rows):
#         print(' ' * (rows - i - 1) + ' *' * (i * 1 + 1))
#
# elif figure == "d":
#     print(*[('* ' * i + '*').rjust(rows * 2 + i) for i in range(rows, 0, -1)],
#           *[('* ' * i + '*').rjust(rows * 2 + i) for i in range(rows + 1)], sep='\n')
#
# elif figure == "e":
#     mat = [[' '] * rows for _ in range(rows)]
#     for i in range(rows):
#         for j in range(rows):
#             if (j < i < rows - 1 - j) or (j > i > rows - 1 - j):
#                 mat[i][j] = '*'
#     for i in mat:
#         print(*i)
#
# elif figure == "j":
#     print(*["* " * i for i in range(rows)], *["* " * i for i in range(rows, 0, -1)], sep='\n')
#
# elif figure == "z":
#     print(*[((rows - i) * ' ' + i * '*') for i in range(rows)], *[(rows - i) * ' ' + i * '*' for i in range(rows, 0, -1)],
#           sep='\n')
#
# elif figure == "i":
#     print("\n".join("* " * i for i in range(rows, 0, -1)))
#
# elif figure == "k":
#     print("\n".join((rows - i) * ' ' + i * '*' for i in range(rows)))
