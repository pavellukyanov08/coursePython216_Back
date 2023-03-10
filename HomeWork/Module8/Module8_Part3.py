# Task 1
basket_players = {
    'Cobi Brayan': 209,
    'Dan Smith': 200,
    'Martin Dodge': 201
}
print(basket_players)

while True:
    command = int(input('Select command (1 - add, 2 - remove, 3 - find, 4 - replace, 0 - exit): '))

    if command == 1:
        name = input('Enter name of player: ')
        height = int(input('Enter height of player: '))

        basket_players[name] = height

        print(f'Players: {name}, height: {height}sm was successfully added')
        # print(basket_players)

    elif command == 2:
        name = input('Enter name of player: ')
        if name in basket_players:
            del basket_players[name]
            print(f'Player {name} was successfully removed')
            print(basket_players)
        else:
            print('Something went wrong')

    elif command == 3:
        name = input('Enter the name of player: ')

        match_player = []   # создаем список для имен
        for key in basket_players.keys():   # итерируемся по нему
            if name in key:
                match_player.append(key)    # если введеное имя есть в словаре, добавляем его в список
        print('List of player:', match_player)

        if match_player:
            if len(match_player) == 1:  # если имена в списке уникально, то берем и выводим его
                player_name = match_player[0]
                print(f'{match_player} is {basket_players[player_name]}')
            else:
                print('Match players are: ')
                for player in match_player:
                    print(f'{player} is {basket_players[player]}')
                print()
        else:
            print('Player not found')

    elif command == 4:
        print(basket_players)

        old_player = input('Enter an existing player: ').capitalize()
        new_player = input('Enter a new player: ').capitalize()

        if old_player in basket_players.keys():
            basket_players.pop(old_player)
            basket_players[new_player] = input(f'Enter the height of {new_player}: ').capitalize()
            print(basket_players)
        else:
            print('Player is not found')


# Task 2
# book_collection = {
#     "Война и мир": {
#         'Автор': 'Лев Толстой',
#         'Жанр': 'Роман',
#         'Год публикации': 1867,
#         'Страницы': 1000,
#
#     }
# }
# print(book_collection)