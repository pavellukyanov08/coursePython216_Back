# Task 1
# countries = {'USA', 'UK', 'Finland', 'Norway'}
# print(countries)
#
# while True: match command := int(input('Select command (1 - add, 2 - remove, 3 - find by symb, 4 - find country,
# 0 - exit): ')):
#
#         case 1:
#             countries.add(input('Enter the country: '))
#
#         case 2:
#             countries.discard(input('Enter the country: '))
#
#         case 3:
#             find_country = input('Enter the country: ')
#             for c in countries:
#                 if find_country in c:
#                     print(c)
#
#         case 4:
#             print(countries.isdisjoint(input('Проверить есть страна: ')))
#
#         case 0:
#             break
#
# print('Program is stopped')


# Task 2
# cities1 = {'Novosibirsk', 'Kiev', 'Minsk', 'Rome'}
# cities2 = {'Madrid', 'Moscow', 'Minsk', 'Rome'}
#
# cities3 = cities1 & cities2
# print(cities3)


# Task 3
# cities1 = {'Novosibirsk', 'Kiev', 'Minsk', 'Rome'}
# cities2 = {'Madrid', 'Moscow', 'Minsk', 'Rome'}
#
# cities3 = cities1.difference(cities2)
# print('Cities, that are in the first set, but not in second set:', cities3)


# Task 4
# cities1 = {'Novosibirsk', 'Kiev', 'Minsk', 'Rome'}
# cities2 = {'Madrid', 'Moscow', 'Minsk', 'Rome'}
#
# cities3 = cities2.difference(cities1)
# print('Cities, that are in the second set, but not in first set:', cities3)


# Task 5
# cities1 = {'Novosibirsk', 'Kiev', 'Rome', 'Rome'}
# cities2 = {'Madrid', 'Moscow', 'Minsk', 'Minsk'}
#
# cities3 = cities1.union(cities2)
# print('Cities unique for each set:', cities3)


# Task 6
country_city = {'Russia': 'Moscow',
                'Spain': 'Madrid',
                'Italy': 'Rome',
                'China': 'Beijing'}

print(country_city)

while True:
    command = int(input('Select command (1 - add, 2 - remove, 3 - find county 4 - replace country, 0 - exit): '))

    if command == 1:
        country = input('Enter name of country: ')
        city = input(f'Enter capital of {country}: ')

        country_city[country] = city
        print(f'Country: {country} and city: {city} was successfully added')
        print(country_city)

    elif command == 2:
        ctr = input('Enter name of country: ')

        if ctr in country_city:
            del country_city[ctr]
            print(f'Country: {ctr} was successfully removed ')
            print(country_city)
        else:
            print('Something went wrong. ')

    elif command == 3:
        print(country_city)
        choice = input('Enter 1, Введите 1, если хотите найти одну столицу\n'
                       'Или 2, если хотите найти все страны и столицы '
                       'по вашему слову: ')

        if choice == 1:
            country = input('Введите страну: ')
            print(f'Столица страны {country} - {country_city[country]}')
        else:
            part_name = input('Введите часть названия страны: ')
            [print(f'Страна: {country}, Столица: {capital}')
             for country, capital in country_city.items() if
             country.startswith(part_name.lower().capitalize())]

    elif command == 4:
        print(country_city)

        old_country = input('Enter an existing country: ').capitalize()
        new_country = input('Enter a new country: ').capitalize()

        if old_country in country_city.keys():
            value = country_city.pop(old_country)
            country_city[new_country] = input(f'Enter the new city of {new_country}: ').capitalize()
            print(country_city)
        else:
            print('Country is not found')

    elif command == 0:
        break

print('Program has been stopped')
