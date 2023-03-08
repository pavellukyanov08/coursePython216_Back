basket_players = {
    'Cobi Brayan': 209
}
print(basket_players)

while True:
    command = int(input('Select command (1 - add, 2 - remove, 3 - find, 4 - replace, 0 - exit): '))

    if command == 1:
        name = input('Enter name of player: ')
        height = int(input('Enter height of player: '))

        basket_players[name] = height

        print(f'Players: {name}, height: {height}sm was successfully added')
        print(basket_players)

    elif command == 2:
        name = input('Enter name of player: ')
        if name in basket_players:
            del basket_players[name]
            print(f'Player {name} was successfully removed')
            print(basket_players)
        else:
            print('Something went wrong')

    elif command == 3:
        find_player = input('Enter the name of player: ')

        for name, height in basket_players.items():
            if name in find_player:
                print(f'Player found -> {name} : {height}')
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


