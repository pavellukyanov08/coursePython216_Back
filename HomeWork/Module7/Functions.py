# Task 1
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# print(gcd(int(input('Введите число: ')), int(input('Введите число: '))))


#Task 2
import random

# функция для создания пустой доски
def create_board():
    board = [[0, 0, 0, 0] for _ in range(4)]
    return board

# функция для вывода доски в консоль
def print_board(board):
    for row in board:
        print(row)

# функция для перемешивания доски
def shuffle_board(board):
    nums = [x for x in range(1, 16)]
    random.shuffle(nums)
    index = 0
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                board[i][j] = 0
            else:
                board[i][j] = nums[index]
                index += 1

# функция для проверки победы
def check_win(board):
    nums = [x for x in range(1, 16)]
    index = 0
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                if board[i][j] != 0:
                    return False
            else:
                if board[i][j] != nums[index]:
                    return False
                index += 1
    return True

# функция для получения координат пустой ячейки
def get_blank_space(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)
    return None

# функция для перемещения ячейки
def move(board, move_dir):
    i, j = get_blank_space(board)
    if move_dir == "up":
        if i == 0:
            return False
        board[i][j] = board[i-1][j]
        board[i-1][j] = 0
        return True
    elif move_dir == "down":
        if i == 3:
            return False
        board[i][j] = board[i+1][j]
        board[i+1][j] = 0
        return True
    elif move_dir == "left":
        if j == 0:
            return False
        board[i][j] = board[i][j-1]
        board[i][j-1] = 0
        return True
    elif move_dir == "right":
        if j == 3:
            return False
        board[i][j] = board[i][j+1]
        board[i][j+1] = 0
        return True
    else:
        return False

# функция для игры
def play_game():
    board = create_board()
    shuffle_board(board)
    print_board(board)
    while True:
        move_dir = input("Введите направление: ")
        if move(board, move_dir):
            print_board(board)
            if check_win(board):
                print("Победа!")
                break
        else:
            print("Неверное направление!")

# запуск игры
play_game()
#В этом коде используются функции для создания пустой доски, вывода доски в консоль, перемешивания доски,
# проверки победы, получения координат пустой ячейки, перемещения ячейки и игры.
# Чтобы начать игру, нужно вызвать функцию `play_game()`.
# Пользователь должен ввести направление (up, down, left, right) для перемещения ячейки.
# Если игрок сделал правильный ход, ячейки будут перемещены в соответствии с направлением.
# Если все ячейки на доске находятся в правильной позиции, игрок победил.
# Если игрок ввел неверное направление, он получит сообщение об ошибке и будет перенаправлен на ввод направления.


