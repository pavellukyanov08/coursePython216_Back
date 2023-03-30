# Task 1
# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# def abbrev_name(name):
#     first, last = name.upper().split()
#     return first[0] + '.' + last[0]
#
#
# print(abbrev_name('Sam Harris'))

# def abbrev_name(name):
#     return '.'.join(n[0] for n in name.split()).upper()
#
#
# print(abbrev_name('Sam Harris'))


# Task 2
# Given an array of integers as strings and numbers,
# return the sum of the array values as if all were numbers.

#
# def sum_mix(arr):
#     return sum(int(n) for n in arr)
#
#
# print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))


# Task 3
# Создайте программу, которая фильтрует список строк и возвращает список, содержащий только имена ваших друзей.
# Если в имени ровно 4 буквы, можете быть уверены, что оно должно быть вашим другом! В противном случае,
# вы можете быть уверены, что он не...
#
# def friend(x):
#     return [x for x in x if len(x) == 4]
#
#
# print(friend(["Ryan", "Kieran", "Mark"]))


# Task 4
# def odd_or_even(arr):
#     return 'even' if sum(arr) % 2 == 0 else 'odd'
#
#
# print(odd_or_even([0, 1, 2, 3, 4, 5]))


# Task 5
# def find_average(numbers):
#     return sum(numbers) / len(numbers)
#
#
# print(find_average([1, 2, 3]))


# Task 6
# def string_to_array(s):
#     return s.split(' ')
#
# print(string_to_array("Robin Singh"))


# Task 7
# def reverse_seq(n):
#     num_list = []
#     for i in range(1, 6):
#         num_list.append(i)
# или     return num_list[::-1]
# или    return list(range(n, 0, -1))
#
#
# print(reverse_seq(5))


# Task 8
# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging
# message :)
# If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".
# def hoop_count(n):
#     return 'Good!' if n >= 10 else 'Keep at it untill you get it'
#
#
# print(hoop_count(11))


# Task 9
# Find min and max number
# def minimum(arr):
#     return min(arr)
#
# def maximum(arr):
#     return max(arr)
#
#
# print(minimum([-52, 56, 30, 29, -54, 0, -110]))
# print(maximum([-52, 56, 30, 29, -54, 0, -110]))


# Task 10
# Write function bmi that calculates body mass index (bmi = weight / height2).
# def bmi(weight, height):
#     bmi = weight / height ** 2
#
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25.0:
#         return "Normal"
#     elif bmi <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"
#
#
# print(bmi(110, 1.80))


# Task 11
# def twice_as_old(dad_years_old, son_years_old):
#     return abs(dad_years_old - son_years_old * 2)
#
#
# print(twice_as_old(42, 21))


# Task 12
# def solution(string):
#     return string[::-1]
#
#
# print(solution('world'))


# Task 13
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd
# argument (also a string).
# def solution(text, ending):
#     return text.endswith(ending)
#
#
# print(solution('abc', 'bc'))


# Task 14
# Your task is to write a function that takes a string
# and return a new string with all vowels removed.
# def disemvowel(string):
#     for sym in 'aeiouAEIOU':
#         string = string.replace(sym, '')
#     return string
#
#
# print(disemvowel('This website is for losers LOL!'))


# Task 15
# def string_to_number(s):
#     return int(s)
#
#
# print(string_to_number("1234"))


# Task 16
# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0
#
# print(paperwork(5, -5))


# Task 17
# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x
#
#
# print(stray([2, 3, 2, 2, 2]))


# def xo(s):
#     return True if
#
#
# print(xo('xo'))


# Task 18
# def find_needle(haystack):
#     return f"found the needle at position {haystack.index('needle')}"
#
#
# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))


# Task 19
# def count_sheep(n):
    # .1
    # sheep = ''
    # for i in range(1, n + 1):
    #     sheep += str(i) + ' sheep...'
    # return sheep

    # 2. return ''.join(f'{i} sheep... ' for i in range(1, n + 1))


# print(count_sheep(5))


# Task 20
# def is_even(n):
#     return True if n % 2 == 0 else False
#
#
# print(is_even(0.5))


# Task 21
# def rental_car_cost(d):
    # return d * 40 - 50 if d >= 7 else d * 40 - 20
    # if d >= 7:
    #     return d * 40 - 50
    # else:
    #     return d * 40 - 20

# print(rental_car_cost(20))


# Task 22
# def how_much_i_love_you(nb_petals):
# return ['i love you ', "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]
print(8 % 6 - 1)
# print(how_much_i_love_you(8))
