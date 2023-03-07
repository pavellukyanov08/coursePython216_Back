from random import randint

# Task 1
# a = tuple(randint(1, 10) for _ in range(7))
# b = tuple(randint(1, 10) for _ in range(7))
# c = tuple(randint(1, 10) for _ in range(7))
#
# print(f'Первый словарь: {a}; второй: {b}; третий: {c}')
# set_a = set(a)
# set_b = set(b)
# set_c = set(c)
#
# intersection = set_a & set_b & set_c
#
# print(f'Общие элементы: {intersection}')


# Task 2
# a = tuple(randint(1, 10) for _ in range(7))
# b = tuple(randint(1, 10) for _ in range(7))
# c = tuple(randint(1, 10) for _ in range(7))
#
# print(f'Первый словарь: {a}; второй: {b}; третий: {c}')
#
# print(set(a))
# print(set(b))
# print(set(c))
t1 = (1, 2, 3, 4, 5, 6, 7, 7)
t2 = (2, 4, 6, 8, 10, 2)
t3 = (1, 3, 5, 7, 9, 1)


def find_unique_el(t):
    unique_elem = set(t)
    return unique_elem


t1_unique = find_unique_el(t1)

t2_unique = find_unique_el(t2)

t3_unique = find_unique_el(t3)

print("Unique elements in tuple 1:", t1_unique)
print("Unique elements in tuple 2:", t2_unique)
print("Unique elements in tuple 3:", t3_unique)