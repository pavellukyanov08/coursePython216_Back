# # def limit_calls(limit):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             nonlocal limit
# #             if limit > 0:
# #                 func(*args, **kwargs)
# #                 limit -= 1
# #             else:
# #                 raise ValueError('Max call limit is reached')
# #         return wrapper
# #     return decorator
# #
# #
# # @limit_calls(2)
# # def print_hello():
# #     print('Hello world')
# #
# #
# # print_hello()
# # print_hello()
# # print_hello()
#
#
# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             all_args = list(args)
#             all_args.extend(list(kwargs.values()))
#             for arg, type_of in zip(all_args, types):
#                 if type_of != type(arg):
#                     raise TypeError(f'Expected {type_of}, got {type(arg)} instead in {arg}')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @validate_args(int, int)
# def summa(a, b):
#     return a + b
#
#
# print(summa(10, 10))


from random import randint
#
# nums = [randint(1, 100) for _ in range(10)]
# print(nums)
#
#
# def binary_search(nums, target):
#     start, end = 0, len(nums)
#     while start <= end:
#         current = (end + start) // 2
#         if nums[current] == target:
#             return current
#         elif nums[current] < target:
#             start = current + 1
#         else:
#             end = current - 1
#     return 'There is not number'
#
#
# print(binary_search(nums, int(input('Введите число: '))))

# nums = [randint(1, 100) for _ in range(10)]
# print(nums)
#
#
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums.pop()
#     left, mid, right = [], [pivot], []
#
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
# print(quick_sort(nums))


import random
def sort_cakes(pancakes):
    j = len(pancakes)
    while j > 0:
        max_r = max(pancakes[:j])
        max_r_index = pancakes.index(max_r)
        pancakes[max_r_index:j] = reversed(pancakes[max_r_index:j])
        j -= 1
        print(pancakes)
        return pancakes[::-1]
        a = [random.randint(1, 10) for i in range(5)]
        print(a)
        print()
        print(sort_cakes(a))
