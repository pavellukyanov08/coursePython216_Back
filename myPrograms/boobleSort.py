num = [8, 7, 6, 5, 4, 3]
counter = 0

for i in range(len(num) - 1):
    for j in range(len(num) - 1):
        if num[j] > num[j + 1]:
            counter += 1
            num[j], num[j + 1] = num[j + 1], num[j]

    print(f'Сортировка: {num}')
print(f'Счетчик: {counter}')
