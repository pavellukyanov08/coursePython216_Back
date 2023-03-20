# Task 1
from random import randint

nums_list = [randint(1, 20) for _ in range(9)]
print('Исходный список:', nums_list)

n = len(nums_list)
arith_mean = sum(nums_list) / n

if arith_mean > 0:
    two_thirds = int(n * 2 / 3)
    sorted_nums = sorted(nums_list[:two_thirds])
    print('Сортировка две трети списка:', sorted_nums)
else:
    first_thirds = int(n / 3)
    sorted_nums = sorted(nums_list[:first_thirds])
    print('Сортировка первой трети списка:', sorted_nums)

unsorted_nums = nums_list[two_thirds:]
reverse_nums = unsorted_nums[::-1]

print('Вывод сортированной части + перевернутой:', sorted_nums + reverse_nums)

