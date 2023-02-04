# while True:
#     figure = input('Выберите фигуру (от 1 до 10, 0 для выхода): ')
#     size = int(input('Введите размер фигуры: '))
#
#     if figure == '0':
#         break
#     elif figure == '5':
#         for i in range(10, 0, -2):
#             print((10 - i) // 2 * ' ' + '*' * i +
#                   (10 - i) // 2 * ' ')
#         for i in range(2, 12, 2):
#             print((10 - i) // 2 * ' ' + '*' * i +
#                   (10 - i) // 2 * ' ')
#         for i in range(10, -10, -2):
#             print((size - abs(i)) // 2 * ' ' + '*' * i +
#                   (size - abs(i)) // 2 * ' * ')
