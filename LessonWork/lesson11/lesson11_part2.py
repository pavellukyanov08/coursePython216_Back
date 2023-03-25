# nums = [1, 2, 3, 4]
# for i in nums:
#     if i == 3:
#         print(i)
#         break
#
#
# def binary_search(nums, key):
#     start, end = 0, len(nums)
#     while start <= end:
#         qurrent = (end + start) // 2
#         if nums[qurrent] == key:
#             return nums[qurrent]
#         elif nums[qurrent] < key:
#             start = qurrent + 1
#         else:
#             end = qurrent - 1
#     return 'There is no number'
#
# from random import randint
#
# nums = sorted([randint(1, 100000) for i in range(100000)])
# print(binary_search(nums, 83258))
#
#
# Сортировка Шелла
# Худшее время O(n^2)
# Лучшее время O(n * log^2n)
# При оптимальном наборе шагов(Седжвика) O(n^(4/3))

# import math
#
#
# def shell_sort(nums):
#     k = int(math.log2(len(nums)))
#     interval = 2**k - 1
#     while interval > 0:
#         for i in range(interval, len(nums)):
#             key = nums[i]
#             j = i
#             while j >= interval and nums[j-interval] > key:
#                 nums[j] = nums[j-interval]
#                 j -= interval
#             nums[j] = key
#         k -= 1
#         interval = 2**k - 1
#
#     return nums
#
#
# def insert_sort(nums):
#     for i in range(1, len(nums)):
#         key = nums[i]
#         j = i
#         while j >= 1 and nums[j-1] > key:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = key
#     return nums
#
#
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums.pop()
#     left, mid, right = [], [pivot], []
#     for num in nums:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             mid.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
#
#
# def pancake_sort(pancakes):
#     sorted_index = 0
#     while pancakes != sorted(pancakes, reverse=True):
#         unsorted_part = pancakes[sorted_index:]
#         max_index = unsorted_part.index(max(unsorted_part))
#
#         top = unsorted_part[max_index:][::-1]
#         unsorted_part = (unsorted_part[:max_index] + top)[::-1]
#
#         pancakes = pancakes[:sorted_index] + unsorted_part
#         sorted_index += 1
#     return pancakes
#
#
# test = False
#
# if test:
#     from random import randint
#     from time import time
#
#     lst = [randint(0, 10000) for i in range(10000)]
#     funcs = [shell_sort, insert_sort, quick_sort, pancake_sort]
#
#     def measure_time(sort_func, array):
#         start = time()
#         sort_func(array)
#         end = time()
#         print(f'{sort_func.__name__} time: ', end - start)
#
#     print('with random nums: ')
#     for func in funcs:
#         measure_time(func, lst.copy())