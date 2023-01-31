num1 = int(input('Введите начала диапазона: '))
num2 = int(input('Введите конец диапазона: '))

for i in range(num1, num2):
    if i % 7 == 0:
        print(f'Числа кратные 7 из диапазона: {i}')