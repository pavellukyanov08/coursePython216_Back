import random

chars = '+_/*!@#$%?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(input('Количество паролей:'))
lenght = int(input('Длинна пароля:'))

for x in range(number):
    password = ''

    for i in range(lenght):
        password += random.choice(chars)

    print(password)
input()
