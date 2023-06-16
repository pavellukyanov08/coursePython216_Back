from abc import ABC, abstractmethod
import math


# Task 1
class Customer:
    def __init__(self):
        self.clients = {}


class Product:
    def __init__(self):
        self.products = {}


class CustomerManager(Customer):
    def add_customer(self, name, birthday, phone):
        self.clients[name] = [birthday, phone]

    def update_customer(self, name, new_birthday, new_phone):
        self.clients[name] = [new_birthday, new_phone]

    @staticmethod
    def get_customer(name, birthday, phone):
        return f'Получены данные: {name} -> {birthday}, {phone} \n'


class ProductInventory(Product):
    def add_customer(self, name, birthday, phone):
        self.products[name] = [birthday, phone]
        return self.products


cm = CustomerManager()

cm.add_customer('John', '16.02.2005', '32048721908471')
cm.update_customer('Michael', '16.02.209', '214729034')
print(cm.get_customer('John', '16.02.2005', '32048721908471'))


# Task 2
class Book:
    def __init__(self, title, author, public_year):
        self.title = title
        self.author = author
        self.public_year = public_year

    def add_book(self):
        print(f'Title: {self.title};   '
              f'Author: {self.author};   '
              f'Year of publication: {self.public_year}')


class FictionBook(Book):
    def __init__(self, title, author, public_year, genre):
        super().__init__(title, author, public_year)
        self.genre = genre

    def add_book(self):
        super().add_book()
        print(f'Жанр: {self.genre}')


class NonFictionBook(Book):
    def __init__(self, title, author, public_year, subject):
        super().__init__(title, author, public_year)
        self.subject = subject

    def add_book(self):
        super().add_book()
        print(f'Субъект: {self.subject}')


class ReferenceBook(Book):
    def __init__(self, title, author, public_year, type):
        super().__init__(title, author, public_year)
        self.type = type

    def add_book(self):
        super().add_book()
        print(f'Тип справочника: {self.type}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_book(self):
        for book in self.books:
            book.add_book()
            print('---' * 20)


lib = Library()

fiction_book = FictionBook("Война и мир", "Лев Толстой", 1867, "Роман")
nonfiction_book = NonFictionBook("Краткая история времени", "Стивен Хокинг", 1988, "Время")
reference_book = ReferenceBook("Чистый код", "Роберт Мартин", 2008, "Программирование на Python")

# Добавление книг в библиотеку
lib.add_book(fiction_book)
lib.add_book(nonfiction_book)
lib.add_book(reference_book)

# Отображение всех книг в библиотеке
lib.print_book()
print()


# Task 3
class Shape(ABC):
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f'Площадь круга: {round(math.pi * self.radius ** 2, 3)}'

    def calculate_perimeter(self):
        return f'Периметр круга: {round(2 * math.pi * self.radius, 3)}'


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return f'Площадь прямоугольника: {self.width * self.height}'

    def calculate_perimeter(self):
        return f'Периметр прямоугольника: {2 * (self.width + self.height)}'


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return f'Площадь треугольника: {math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))}'

    def calculate_perimeter(self):
        return f'Периметр треугольника: {self.a + self.b + self.c}'


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10 ,5)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

triangle = Triangle(3, 4, 5)
print(triangle.calculate_area())
print(triangle.calculate_perimeter())
print()


# Task 4
class TextMessaging:
    @staticmethod
    def send_text_message(message):
        return f'Сообщение: "{message}" было отправлено'

    @staticmethod
    def receive_text_message(receive_msg):
        return f'Вам пришло сообщение -> {receive_msg}'

    @staticmethod
    def get_message_history(all_messages):
        return f'Все сообщения: {all_messages}'


class MultimediaMessaging:
    @staticmethod
    def send_multimedia_message(media_msg):
        return f'Медиа сообщение "{media_msg}" было отправлено'

    @staticmethod
    def receive_multimedia_message(media_msg):
        return f'Вам пришло медиасообщение -> {media_msg}'

    @staticmethod
    def view_media_gallery(all_messages):
        return f'Все медиа сообщения: {all_messages}'


tm = TextMessaging()
print(tm.send_text_message('Hello world'))
print(tm.receive_text_message('Hey, user!'))
print(tm.get_message_history('Hello world, Hey user!\n'))

mm = MultimediaMessaging()
print(mm.send_multimedia_message('Hello world'))
print(mm.receive_multimedia_message('Hey, user!'))
print(mm.view_media_gallery('Hello world, Hey user!'))
print()


# Task 5
class Logger(ABC):
    @abstractmethod
    def log_info(self, info):
        pass

    @abstractmethod
    def log_warning(self, warning):
        pass

    @abstractmethod
    def log_error(self, error):
        pass


class ConsoleLogger(Logger):
    def log_info(self, info):
        return f'Информация: {info}'

    def log_warning(self, warning):
        return f'Предупреждение: {warning}'

    def log_error(self, error):
        return f'Ошибка: {error}'


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log_info(self, info):
        with open(self.filename, 'a') as f:
            f.write(f'Информация: {info}')

    def log_warning(self, warning):
        with open(self.filename, 'a') as f:
            f.write(f'Предупреждение: {warning}')

    def log_error(self, error):
        with open(self.filename, 'a') as f:
            f.write(f'Ошибка: {error}')


class DatabaseLogger(Logger):
    def __init__(self, database):
        self.database = []

    def log_info(self, info):
        self.database.append('Информация')

    def log_warning(self, warning):
        self.database.append('Предупреждение')

    def log_error(self, error):
        self.database.append('Ошибка')


console_logger = ConsoleLogger()
file_logger = FileLogger('log.txt')
database_logger = DatabaseLogger('database')

print(console_logger.log_info('Something info'))
print(console_logger.log_warning('Something warning'))
print(console_logger.log_error('Something error'))
