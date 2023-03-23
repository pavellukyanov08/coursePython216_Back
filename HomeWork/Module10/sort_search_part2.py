# # Task 1
# users_guide = {1: 89643274819, 2: 897687958371, 3: 89671049281, 4: 89090192859, 5: 89010121049}
# print(users_guide)
#
# while True:
#     command = int(input('Введите команду: (1 - сортировка по ID, 2- сортировка по номеру, 3 - вывод id и номеров, '
#                         '4 - выход): '))
#
#     if command == 1:
#         print(sorted(users_guide.keys()))
#
#     elif command == 2:
#         print(sorted(users_guide.values()))
#
#     elif command == 3:
#         print(users_guide.items())
#
#     else:
#         break
#
# print('Программа завершена')


# Task 2
books = {'Война и мир': 1867, 'Анна Каренина': 1873, 'Отцы и дети': 1862, 'Муму': 1854, 'Евгений Онегин': 1833}
print(books)

while True:
    command = int(input('Введите команду: (1 - сортировка по названию, 2- сортировка по году выпуска, 3 - вывод '
                        'названия и дат, 4 - выход): '))

    if command == 1:
        print(sorted(books.keys()))

    elif command == 2:
        print(sorted(books.values()))

    elif command == 3:
        print(books.items())

    else:
        break

print('Программа завершена')
