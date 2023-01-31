# Task1
num = int(input('Введите число: '))

for i in range(1, num + 1):
    if i % 7 == 0:
        print(f'Число, кратное 7 из диапазона: {i}')
