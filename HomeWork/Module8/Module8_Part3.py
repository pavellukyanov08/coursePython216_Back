# basket_players1 = {'name': 'Arvydas Sabonis', 'height': 221}
# basket_players2 = {'name': 'Ralph Sampson', 'height': 224}
# basket_players3 = {'name': 'Ya Min', 'height': 229}
# print(f'{basket_players1}; \n{basket_players2}; \n{basket_players3}')


# basket_players = {}
#
# print(basket_players)
#
# while True:
#     match command := int(input('Select command (1 - add, 2 - find, 3 - remove, 4 - replace, 0 - exit): ')):
#
#         case 1:
#             name = input('Enter name of player: ')
#             height = int(input('Enter height of basketball player: '))
#
#             basket_players.update({'name': name, 'height': height})
#
#             print(f'Players: {name}, height: {height}sm was successfully added')
#             print(basket_players)
#
#         case 2:
#             name = input('Enter name of player: ')
#             height = basket_players[name]
#
#             for n in basket_players.items():
#                 if name in n:
#                     print(f"Player: {name}, height: {height}sm")
#                 else:
#                     print(f"Player {name} not found")
#
#             if name in basket_players:
#                 height = basket_players['name']
#                 print(f"Player: {name}, height: {height}sm")
#             else:
#                 print(f"Player {name} not found")
#
#         case 3:
#             name = input('Enter thr name: ')
#             basket_players.pop(name)
#
#         case 4:
#             name = input('Enter current name: ')
#             new_name = input('Enter new name: ')
#
#             height = basket_players['name']
#
#             for value in basket_players:
#                 basket_players.update({new_name: height})
#         case 0:
#             break
#
# print('Program is stopped')
# def remove_players():
#     for name in basket_players:
#         if name in basket_players:
#             print('Players {name} has a height of {height}')
#         else:
#             print('Players {name} not found')


# add_players()
# search_players()
# remove_players()
