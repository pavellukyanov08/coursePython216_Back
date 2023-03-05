# a = {3: '5', 1: 10}
#
# for key, value in a.items():
#     print(f'{key}: {value}')


# Task 1
# my_dict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# res = 1
# for value in my_dict.values():
#     res *= value


# Task 2
# vegetables = dict([(i, input('Введите 4 овоща: ')) for i in range(1, 5)])
# print(vegetables)
#
# del vegetables[int(input(''))]

# for i in range(1, 5):
#     veg_inpt = input('Введите 4 овоща: ')
#     vegetables[i] = veg_inpt
# print(vegetables)
#
# vegetables.pop(int(input('Введите, что удалить: ')))
# print(vegetables)


# Task 3
# x, y = {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
#
# x.update(y)
# print(x)


# Task 4
# people = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# name_salary = {'name': people.pop('name'), 'salary': people.pop('salary')}
# print(name_salary)
# print(people)


# Task 5
# people = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# people['location'] = people.pop('city')
# print(people)


# Task 6
a = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

dict_data = list(a.items())[:2]
print(dict(dict_data))