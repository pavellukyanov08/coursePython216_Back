# Task 1

# pip install faker
# from faker import Faker
import random

# Вывод на русском
# faker = Faker('ru-RU')
#
# length_list = int(input('Введите длину списка: '))
# names = [faker.first_name_male() for _ in range(length_list)]
# heights = [random.randint(170, 210) for _ in range(length_list)]
#
# names_heights = dict(zip(names, heights))
# print(f'Словарь: {names_heights}')
#
# sorted_names = dict(sorted(names_heights.items(), key=lambda height: height[1], reverse=True))
# print(f'Отсортированный список: {list(sorted_names.keys())}')


# Task 2
# nums = [random.randint(0, 100) for _ in range(10) for _ in range(10)]
# print(nums)
#
# good_pair_counter = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j] and i < j:
#             good_pair_counter += 1
# print(good_pair_counter)


# Task 3
# nums = [random.randint(0, 100) for _ in range(10) for _ in range(10)]
#
# result = []
# counter = 0
#
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j and nums[j] < nums[i]:
#             counter += 1
#         result.append(counter)
# print(result)

#Task 3
# nums = [random.randint(0, 100) for _ in range(int(input('Введите длину списка: ')))]
# print(f'Исходные числа: {nums}')
#
# result_list = []
# counter = 0
#
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j and nums[j] < nums[i]:
#             counter += 1
#     result_list.append(counter)
# print(f'Вывод: {result_list}')