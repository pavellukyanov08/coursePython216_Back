import json
import pickle
#
#
# class Car:
#     def __init__(self, model, year_release, manufacturer, eng_cap, color, price):
#         self.model = model
#         self.year_release = year_release
#         self.manufacturer = manufacturer
#         self.eng_cap = eng_cap
#         self.color = color
#         self.price = price
#
#     def input_data(self):
#         self.model = input('Введите модель: ')
#         self.year_release = int(input('Введите дату релиза: '))
#         self.manufacturer = input('Введите производителя: ')
#         self.eng_cap = float(input('Введите объем двигателя: '))
#         self.color = input('Введите цвет машины: ')
#         self.price = int(input('Введите цену: '))
#
#     def output_data(self):
#         print(f'\nМодель: {self.model};'
#               f'\n год выпуска: {self.year_release};'
#               f'\n производитель: {self.manufacturer};'
#               f'\n объем двигателя: {self.eng_cap};'
#               f'\n цвет машины: {self.color};'
#               f'\n цена: {self.price}')
#
#     def packing_json(self, filename):
#         data = {
#             'model': self.model,
#             'year_release': self.year_release,
#             'manufacturer': self.manufacturer,
#             'eng_cap': self.eng_cap,
#             'color': self.color,
#             'price': self.price
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#
#     def unpacking_json(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             self.model = data['model']
#             self.year_release = data['year_release']
#             self.manufacturer = data['manufacturer']
#             self.eng_cap = data['eng_cap']
#             self.color = data['color']
#             self.price = data['price']
#
#     def packing_pickle(self, filename):
#         data = {
#             'model': self.model,
#             'year_release': self.year_release,
#             'manufacturer': self.manufacturer,
#             'eng_cap': self.eng_cap,
#             'color': self.color,
#             'price': self.price
#         }
#         with open(filename, 'wb') as f:
#             pickle.dump(data, f)
#
#     def unpacking_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             data = pickle.load(f)
#             self.model = data['model']
#             self.year_release = data['year_release']
#             self.manufacturer = data['manufacturer']
#             self.eng_cap = data['eng_cap']
#             self.color = data['color']
#             self.price = data['price']
#
#
# car1 = Car('', '', '', '', '', '')
#
# car1.input_data()
# car1.output_data()
#
# car1.packing_json('car.json')
# car1.packing_pickle('car.pkl')
#
# car1.unpacking_json('car.json')
# car1.unpacking_pickle('car.pkl')


# Task 2
# class Book:
#     def __init__(self, name, year_release, publisher, genre, author, price):
#         self.name = name
#         self.year_release = year_release
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def input_data(self):
#         self.name = input('Введите название: ')
#         self.year_release = int(input('Введите год выпуска: '))
#         self.publisher = input('Введите издателя: ')
#         self.genre = input('Введите жанр: ')
#         self.author = input('Введите автора: ')
#         self.price = int(input('Введите цену: '))
#
#     def output_data(self):
#         print(f'\nНазвание: {self.name};'
#               f'\n год выпуска: {self.year_release};'
#               f'\n издатель: {self.publisher};'
#               f'\n жанр: {self.genre};'
#               f'\n автор: {self.author};'
#               f'\n цена: {self.price}')
#
#     def packing_json(self, filename):
#         data = {
#             'name': self.name,
#             'year_release': self.year_release,
#             'publisher': self.publisher,
#             'genre': self.genre,
#             'author': self.author,
#             'price': self.price
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#
#     def unpacking_json(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             self.name = data['name']
#             self.year_release = data['year_release']
#             self.publisher = data['publisher']
#             self.genre = data['genre']
#             self.author = data['author']
#             self.price = data['price']
#
#     def packing_pickle(self, filename):
#         data = {
#             'name': self.name,
#             'year_release': self.year_release,
#             'publisher': self.publisher,
#             'genre': self.genre,
#             'author': self.author,
#             'price': self.price
#         }
#         with open(filename, 'wb') as f:
#             pickle.dump(data, f)
#
#     def unpacking_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             data = pickle.load(f)
#             self.name = data['name']
#             self.year_release = data['year_release']
#             self.publisher = data['publisher']
#             self.genre = data['genre']
#             self.author = data['author']
#             self.price = data['price']
#
#
# book1 = Book('', '', '', '', '', '')
#
# book1.input_data()
# book1.output_data()
#
# book1.packing_json('book.json')
# book1.packing_pickle('book.pkl')
#
# book1.unpacking_json('book.json')
# book1.unpacking_pickle('book.pkl')
#
#
# # Task 3
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input('Введите название: ')
        self.opening_date = input('Введите дату открытия (дд.мм.гг): ')
        self.country = input('Введите страну: ')
        self.city = input('Введите город: ')
        self.capacity = int(input('Введите вместимость стадиона: '))

    def output_data(self):
        print(f'\nНазвание: {self.name};\n дата открытия: {self.opening_date};\n страна: {self.country};\n '
              f'город: {self.city};\n вместимость стадиона: {self.capacity}')

    def packing_json(self, filename):
        data = {
            'name': self.name,
            'opening_date': self.opening_date,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity,
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def unpacking_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.name = data['name']
            self.opening_date = data['opening_date']
            self.country = data['country']
            self.city = data['city']
            self.capacity = data['capacity']

    def packing_pickle(self, filename):
        data = {
            'name': self.name,
            'opening_date': self.opening_date,
            'country': self.country,
            'city': self.city,
            'capacity': self.capacity,
        }
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def unpacking_pickle(self, filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            self.name = data['name']
            self.opening_date = data['opening_date']
            self.country = data['country']
            self.city = data['city']
            self.capacity = data['capacity']


stadium1 = Stadium('', '', '', '', '')

stadium1.input_data()
stadium1.output_data()

stadium1.packing_json('stadium.json')
stadium1.packing_pickle('stadium.pkl')

stadium1.unpacking_json('stadium.json')
stadium1.unpacking_pickle('stadium.pkl')
