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
def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


print(odd_or_even([0, 1, 2, 3, 4, 5]))


