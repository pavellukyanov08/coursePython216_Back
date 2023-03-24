# Task 1
num = [8, 7, 6, 5, 4, 3]
print('Начальный список:', num)

middle = len(num) // 2

first = sorted(num[:middle], reverse=True)
second = sorted(num[middle:])

print(f'Объединение: {first + second}')



# Task 2
# num = [8, 7, 6, 5, 4, 3]
# print(num)
# for i in range(1, len(num)):
#     temp = num[i]
#     j = i - 1
#     while j >= 0 and temp < num[j]:
#         num[j + 1] = num[j]
#         j = j - 1
#     num[j + 1] = temp
#
# print('Sorted list: ', end='')
# print()


