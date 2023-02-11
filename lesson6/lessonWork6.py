# lst = [1, 2, 3]
# lst.append() - Добавить один элемент в конец
# lst.extend() - Добавить много элементов в конец
# lst.insert() - Добавить один элемент в любое место

# lst.pop() - Удалить элемент по индексу
# lst.remove() - Удалить элемент по значению
# lst.clear() - Удалить все элементы из списка

# lst.count() - Посчитать количество повторений элемента
# lst.copy() - Сделать копию списка
# lst.index() - Возвращает индекс первого вхождения элемента
# lst.sort() - Сортирует в порядке возрастания
# lst.reverse() - Переворачивает список


import random
# Task 1

# nums = [int(input('--> ')) for i in range(int(input('Введите элемент списка: \nn= ')))]
# nums.pop(int(input('Введите индекс:\nk= ')))
# print(nums)


# Task 2

# nums = [int(input('--> ')) for i in range(int(input('Введите элемент списка: n= ')))]
# nums.remove(int(input('Введите элемент:\nk= ')))
# nums.sort()
# print(nums[::-1])


# Task 3

# random_nums = [random.randint(0, 100) for i in range(10)]
# print(f'Все числа: {random_nums}')
#
# print(f'Max: {max(random_nums)}')
#
# random_nums.insert(0, random_nums.pop(random_nums.index(max(random_nums))))
# print(random_nums)


# Task 4

# rng_nums = [random.randint(-10, 10) for i in range(10)]
# negative_nums = []
# print(rng_nums)
# for num in rng_nums[::-1]:
#     if num < 0:
#         negative_nums.append(num)
#         rng_nums.remove(num)
# rng_nums += negative_nums
# print(rng_nums)

# 2 Решение
# rng_nums = [random.randint(-10, 10) for i in range(10)]
# print(rng_nums)
# for i in range(len(rng_nums) - 1, -1, -1):
#     if rng_nums[i] < 0:
#         rng_nums.append(rng_nums.pop(i))
# print(rng_nums)


# Task 5
# random_nums = [randint(0, 100) for i in range(10)]
# minimum = min(random_nums)
# print(random_nums)
#
# index_min = random_nums.index(minimum)
#
# print(f'Min: {minimum}')
# print(f'Index of minimum: {index_min}')

# random_nums = random_nums[index_min:]
# print(random_nums)


# Task 6
# num_list1 = [randint(0, 50) for i in range(int(input('Введите количество элементов 1 списка: ')))]
# num_list2 = [randint(0, 50) for j in range(int(input('Введите количество элементов 2 списка: ')))]
# num_list3 = num_list1 + num_list2
#
# print(f'Список 1: {num_list1}')
# print(f'Cписок 2: {num_list2}', '\n')
#
# print(f'1) Общий список: {num_list3}')
#
# num_list3 = [i for i in num_list1 if i not in num_list2] + [j for j in num_list2 if j not in num_list1]
# print(f'2) Общий список без повторений: {num_list3}')
#
# num_list3 = [i for i in num_list1 if i not in num_list2] + [j for j in num_list2 if j not in num_list1]
# print(f'3) {num_list3}')
#
# print(f'4) Мин. 1 список: {min(num_list1)}; Макс. 2 список: {max(num_list1)}; Мин. 2 список: {min(num_list2)};
# Макс. 2 ' f'список: {max(num_list2)}')


# Task 7
# my_list = []
# length = int(input('Введите длину списка(0-10): '))
# while len(my_list) < length:
#     rng = random.randint(0, 9)
#     if rng not in my_list:
#         my_list.append(rng)
# print(my_list)

# Решение с методом sample
print(random.sample(range(0, 10), 10))
