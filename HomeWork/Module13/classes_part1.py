# Task 1
class Car:
    def __init__(self, model, year_release, manufacturer, eng_cap, car_clr, price):
        self.__model = model
        self.year_release = year_release
        self.__manufacturer = manufacturer
        self.eng_cap = eng_cap
        self.car_clr = car_clr
        self.price = price

    @property
    def input_model(self):
        return self.__model

    @input_model.setter
    def input_model(self, model):
        self.__model = model

    @property
    def input_manufacturer(self):
        return self.__manufacturer

    @input_manufacturer.setter
    def input_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @input_model.setter
    def input_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer
        return self.manufacturer

    def input_data(self):
        # self.model = input('Введите модель: ')
        self.year_release = int(input('Введите дату релиза: '))
        # self.manufacturer = input('Введите производителя: ')
        self.eng_cap = float(input('Введите объем двигателя: '))
        self.car_clr = input('Введите цвет машины: ')
        self.price = int(input('Введите цену: '))

    def output_data(self):
        print(f'\nМодель: {self.model};\n год выпуска: {self.year_release};\n производитель: {self.manufacturer};\n '
              f'объем двигателя: {self.eng_cap};\n цвет машины: {self.car_clr};\n цена: {self.price}')


car1 = Car('', '', '', '', '', '')

car1.model = 'M5'
car1.manufacturer = 'BMW'

car1.input_data()
car1.output_data()


# Task 2
class Book:
    def __init__(self, name, year_release, publisher, genre, author, price):
        self.__name = name
        self.year_release = year_release
        self.publisher = publisher
        self.genre = genre
        self.__author = author
        self.price = price

    @property
    def input_name(self):
        return self.__name

    @property
    def input_author(self):
        return self.__author

    @input_name.setter
    def input_name(self, name):
        self.__name = name

    @input_author.setter
    def input_publisher(self, author):
        self.__author = author

    def input_data(self):
        # self.name = input('Введите название: ')
        self.year_release = int(input('Введите год выпуска: '))
        self.publisher = input('Введите издателя: ')
        self.genre = input('Введите жанр: ')
        # self.author = input('Введите автора: ')
        self.price = int(input('Введите цену: '))

    def output_data(self):
        print(f'\nМодель: {self.name};\n год выпуска: {self.year_release};\n издатель: {self.publisher};\n '
              f'объем двигателя: {self.genre};\n цвет машины: {self.author};\n цена: {self.price}')


book1 = Book('', '', '', '', '', '')

book1.name = 'Война и мир'
# print(stadium1.name)

book1.author = 'Лев Толстой'
# print(stadium1.opening_date)

book1.input_data()
book1.output_data()


# Task 3
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    @property
    def input_name(self):
        return self.__name

    @property
    def input_opening_date(self):
        return self.__opening_date

    @input_name.setter
    def input_name(self, name):
        self.__name = name

    @input_opening_date.setter
    def input_opening_date(self, opening_date):
        self.__opening_date = opening_date

    def input_data(self):
        # self.name(input('Введите название: '))
        # self.opening_date(input('Введите дату открытия (дд.мм.гг): '))
        self.country = (input('Введите страну: '))
        self.city = (input('Введите город: '))
        self.capacity = (int(input('Введите вместимость стадиона: ')))

    def output_data(self):
        print(f'\nНазвание: {self.name};\n дата открытия: {self.opening_date};\n страна: {self.country};\n '
              f'город: {self.city};\n вместимость стадиона: {self.capacity}')


stadium1 = Stadium('', '', '', '', '')

stadium1.name = 'Арена славы'
# print(stadium1.name)

stadium1.opening_date = '22.02.22'
# print(stadium1.opening_date)

stadium1.input_data()
stadium1.output_data()
