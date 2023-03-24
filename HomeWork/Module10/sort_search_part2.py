# # Task 1
# users_guide = {1: 89643274819, 2: 897687958371, 3: 89671049281, 4: 89090192859, 5: 89010121049}
# print(users_guide)

# 1. Using dictionaries
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


# 2. Using lists
# user_id = [1, 2, 3, 4, 5]
# user_number = [89643274819, 897687958371, 89671049281, 89090192859, 89010121049]
#
# user_guide = {}
#
# while True:
#     command = int(input('Select a command: (1 - sort by ID, 2 - sort by phone number, '
#                         '3 - output ID and phone number, '
#                         '4 - exit): '))
#
#     if command == 1:
#         for i in range(len(user_id)):
#             user_guide[user_id[i]] = user_number[i]
#
#         sorted_user_guide = sorted(user_guide)
#         print('Sort by ID:', sorted_user_guide)
#
#         for user in sorted_user_guide:
#             print(f' User ID: {user} -> Phone number: {user_guide[user]}')
#
#     elif command == 2:
#         for i in range(len(user_number)):
#             user_guide[user_number[i]] = user_id[i]
#
#         sorted_user_guide = sorted(user_guide)
#         print('Sort by phone number:', sorted_user_guide)
#
#         for number in sorted_user_guide:
#             print(f'Phone number: {number} -> User ID: {user_guide[number]}')
#
#     elif command == 3:
#         for i in range(len(user_id)):
#             print(f'User ID: {user_id[i]} --> Phone number: {user_number[i]}')
#
#     else:
#         break
#
# print('Program is completed')


# Task 2
# books = {'Война и мир': 1867, 'Анна Каренина': 1873, 'Отцы и дети': 1862, 'Муму': 1854, 'Евгений Онегин': 1833}
# print(books)
#
# Using dictionaries
# while True:
#     command = int(input('Введите команду: (1 - сортировка по названию, 2- сортировка по году выпуска, 3 - вывод '
#                         'названия и дат, 4 - выход): '))
#
#     if command == 1:
#         print(sorted(books.keys()))
#
#     elif command == 2:
#         print(sorted(books.values()))
#
#     elif command == 3:
#         print(books.items())
#
#     else:
#         break
#
# print('Программа завершена')


# 2. Using lists
book_name = ['Война и мир', 'Анна Каренина', 'Отцы и дети', 'Муму', 'Евгений Онегин']
year_publish = [1867, 1873, 1862, 1854, 1833]

books = {}

while True:
    command = int(input('Select a command: (1 - sort by book name, 2 - sort by year publish, '
                        '3 - output book name and year publish, '
                        '4 - exit): '))

    if command == 1:
        for i in range(len(book_name)):
            books[book_name[i]] = year_publish[i]

        sorted_books = sorted(books)
        print('Sort by book name:', sorted_books)

        for name in sorted_books:
            print(f'Book name: {name} -> Year publish: {books[name]}')

    elif command == 2:
        for i in range(len(year_publish)):
            books[year_publish[i]] = book_name[i]

        sorted_books = sorted(books)
        print('Sort by year publish:', sorted_books)

        for year in sorted_books:
            print(f'Year publish: {year} -> Book name: {books[year]}')

    elif command == 3:
        for i in range(len(book_name)):
            print(f'Book name: {book_name[i]} --> Year publish: --> {year_publish[i]}')

    else:
        break

print('Program is completed')
