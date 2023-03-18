import random

chars = '+_/*!@#$%?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for _ in range(int(input('Количество паролей:'))):
    password = ''

    for _ in range(int(input('Длинна пароля:'))):
        password += random.choice(chars)

    print(password)
