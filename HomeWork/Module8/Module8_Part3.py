# Task 1
# basket_players = {
#     'Cobi Brayan': 209,
#     'Dan Smith': 200,
#     'Martin Dodge': 201
# }
# print(basket_players)
#
# while True:
#     command = int(input('Select command (1 - add, 2 - remove, 3 - find, 4 - replace, 0 - exit): '))
#
#     if command == 1:
#         name = input('Enter name of player: ')
#         height = int(input('Enter height of player: '))
#
#         basket_players[name] = height
#
#         print(f'Players: {name}, height: {height}sm was successfully added')
#         # print(basket_players)
#
#     elif command == 2:
#         name = input('Enter name of player: ')
#         if name in basket_players:
#             del basket_players[name]
#             print(f'Player {name} was successfully removed')
#             print(basket_players)
#         else:
#             print('Something went wrong')
#
#     elif command == 3:
#         print(basket_players)
#         choice = input('Enter 1, if you want to find one player, or 2, if you want to find all players by you word: ')
#
#         if choice == 1:
#             name = input('Enter the name of player: ')
#             print(f'Player: {name} - > {basket_players[name]}')
#
#         else:
#             part_name = input('Enter part of name player: ')
#             [print(f'Player: {name}, height: {height}')
#              for name, height in basket_players.items() if name.startswith(part_name.lower().capitalize())]
#
#     elif command == 4:
#         print(basket_players)
#
#         old_player = input('Enter an existing player: ').capitalize()
#         new_player = input('Enter a new player: ').capitalize()
#
#         if old_player in basket_players.keys():
#             basket_players.pop(old_player)
#             basket_players[new_player] = input(f'Enter the height of {new_player}: ').capitalize()
#             print(basket_players)
#         else:
#             print('Player is not found')

# Task 2
book_collection = {
    "Война и мир": {
        'Автор': 'Лев Толстой',
        'Жанр': 'Роман',
        'Год публикации': 1867,
        'Страницы': 1000
    }
}
print(book_collection)

while True:
    command = int(input('Select command (1 - add, 2 - remove, 3 - find, 4 - replace, 0 - exit): '))

    if command == 1:
        name_book = input('Введите название книги: ')

        author = input('Введите автора: ')
        genre = input('Введите жанр: ')
        year = input('Введите год: ')
        pages = input('Введите кол-во страниц: ')
        publisher = input('Введите издательство: ')

        book_collection[name_book] = {
            'Автор': author,
            'Жанр': genre,
            'Год': year,
            'Кол-во страниц': pages,
            'Издательство': publisher
        }

        print(book_collection)

    elif command == 2:
        name_book = input('Enter name of book: ')

        if name_book in book_collection:
            del book_collection[name_book]
            print(f'Book: {name_book} was successfully removed ')
            print(book_collection)
        else:
            print('Something went wrong. ')

    elif command == 3:
        print(book_collection)

        search_title = input('Введите название книги: ')
        [print(f'{author} -> {title}')
            for title, author in book_collection.items()
            if title.startswith(search_title.lower().capitalize())]

    elif command == 4:
        title = input("Введите название книги, которую нужно заменить: ")
        new_title = input('Введите название новой книги: ')

        if title in book_collection.keys():
            value = book_collection.pop(title)
            book_collection[new_title] = {
                'Автор': input("Автор: "),
                'Жанр': input("Жанр: "),
                'Год издания': input("Год выпуска: "),
                'Кол-во страниц': input("Количество страниц: "),
                'Издатель': input("Издательство: ")
            }

            print("Данные о книге успешно изменены, новый словарь: ", book_collection)
        else:
            print("Книга с таким названием не найдена в коллекции")

    elif command == 0:
        break
