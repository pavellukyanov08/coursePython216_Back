# # Task 1
# from abc import ABC, abstractmethod

#
# # Абстрактный класс Command
# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# # Конкретный класс для команды "Открыть дверь"
# class OpenDoorCommand(Command):
#     def __init__(self, door):
#         self.door = door
#
#     def execute(self):
#         self.door.open()
#
#
# # Конкретный класс для команды "Закрыть дверь"
# class CloseDoorCommand(Command):
#     def __init__(self, door):
#         self.door = door
#
#     def execute(self):
#         self.door.close()
#
#
# # Класс, управляющий командами
# class Invoker:
#     def __init__(self):
#         self.commands = []
#
#     def add_command(self, command):
#         self.commands.append(command)
#
#     def execute_commands(self):
#         for command in self.commands:
#             command.execute()
#
#
# # Класс, представляющий дверь
# class Door:
#     def __init__(self, name):
#         self.name = name
#
#     def open(self):
#         print(f"{self.name} открыта")
#
#     def close(self):
#         print(f"{self.name} закрыта")
#
#
# # Создаем объекты команд
# door1 = Door("Дверь №1")
# open_command1 = OpenDoorCommand(door1)
# close_command1 = CloseDoorCommand(door1)
#
# door2 = Door("Дверь №2")
# open_command2 = OpenDoorCommand(door2)
# close_command2 = CloseDoorCommand(door2)
#
# # Создаем объект Invoker и добавляем команды
# invoker = Invoker()
# invoker.add_command(open_command1)
# invoker.add_command(close_command1)
# invoker.add_command(open_command2)
# invoker.add_command(close_command2)
#
# # Выполняем команды
# invoker.execute_commands()
#
# door1 = Door('Дверь №1')
# open_command1 = OpenDoorCommand(door1)
# close_command1 = CloseDoorCommand(door1)
#
# door2 = Door("Дверь №2")
# open_command2 = OpenDoorCommand(door2)
# close_command2 = CloseDoorCommand(door2)
#
# # Создаем объект Invoker и добавляем команды
# invoker = Invoker()
# invoker.add_command(open_command1)
# invoker.add_command(close_command1)
# invoker.add_command(open_command2)
# invoker.add_command(close_command2)
#
# # Выполняем команды
# invoker.execute_commands()


# from abc import ABC, abstractmethod


# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# class PrintCommand(Command):
#     def __init__(self, message):
#         self.message = message
#
#     def execute(self):
#         print(self.message)
#
#
# class Calculator:
#     def __init__(self):
#         self._current = 0
#
#     def add(self, value):
#         self._current += value
#
#     def sub(self, value):
#         self._current -= value
#
#     def mult(self, value):
#         self._current *= value
#
#     def div(self, value):
#         self._current /= value
#
#     def get_current_value(self):
#         return self._current
#
#
# class AddCommand:
#     def __init__(self, calculator, value):
#         self.calculator = calculator
#         self.value = value
#
#     def execute(self):
#         self.calculator.add(self.value)
#
#
# class SubCommand:
#     def __init__(self, calculator, value):
#         self.calculator = calculator
#         self.value = value
#
#     def execute(self):
#         self.calculator.sub(self.value)
#
#
# class MultCommand:
#     def __init__(self, calculator, value):
#         self.calculator = calculator
#         self.value = value
#
#     def execute(self):
#         self.calculator.sub(self.value)
#
#
# class DivCommand:
#     def __init__(self, calculator, value):
#         self.calculator = calculator
#         self.value = value
#
#     def execute(self):
#         self.calculator.sub(self.value)
#
#
# calc = Calculator()
#
# commands = [
#     AddCommand(calc, 10),
#     SubCommand(calc, 7),
#     SubCommand(calc, 5),
#     DivCommand(calc, 12),
#     PrintCommand(calc.get_current_value())
# ]
#
# for command in commands:
#     command.execute()
#
# print("Final value:", calc.get_current_value())


# Task 2
# class GetNumbers:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def get_numbers(self):
#         with open(self.filename, 'r', encoding='utf-8') as f:
#             numbers = [int(line) for line in f]
#             return numbers
#
#
# class ProxyNumbers:
#     def __init__(self, filename, logs_file):
#         self.filename = filename
#         self.numbers = GetNumbers(self.filename).get_numbers()
#         self.logs_file = logs_file
#
#     @staticmethod
#     def logging(func):
#         def wrapper(self, *args, **kwargs):
#             with open(self.logs_file, 'a', encoding='utf-8') as f:
#                 f.write(f'Был вызван метод {func.__name__}\n')
#             return func(self, *args, **kwargs)
#         return wrapper
#
#     @logging
#     def get_sum(self):
#         return f'Сумма чисел: {sum(self.numbers)}'
#
#     @logging
#     def get_max(self):
#         return f'Максимальное число: {max(self.numbers)}'
#
#     @logging
#     def get_min(self):
#         return f'Минимальное число: {min(self.numbers)}'
#
#
# log = ProxyNumbers('numbers.txt', 'log.txt')
#
# print(log.get_max())
# print(log.get_min())
# print(log.get_sum())


# Task 3
import json


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_reader(self, name):
        self.readers.append(name)

    def remove_reader(self, name):
        self.readers.append(name)

    def find_readers(self, name):
        result = []
        for reader in self.readers:
            if name is None or reader.name == name:
                result.append(reader)
        return result

    def save_readers(self, filename):
        with open(filename, "w") as f:
            data = {
                "readers": [
                    [{'name': reader.name, 'books': [book.title for book in reader.books]} for reader in
                        self.readers]
                ],
                "books": [
                    {'title': book.title, 'author': book.author, 'year': book.year, 'is_available': book.is_available}
                    for book in self.books]
            }
            json.dump(data, f)
        self.log.info(f"Library data was saved to {filename}")

    def load_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            books_data = data['books']

            for book_data in books_data:
                book = Book(book_data['title'], book_data['author'], book_data['year'])
                book.is_available = book_data['is_available']
                self.add_book(book)

            readers_data = data['readers']
            for reader_data in readers_data:
                reader = Reader(reader_data['name'])
                self.add_reader(reader)
                for book_title in reader_data['books']:
                    books = self.find_books(title=book_title, available_only=False)
                    if books:
                        reader.books.append(books[0])
                        books[0].is_available = False

        self.log.info(f"Library data was loaded from {filename}")


class Reader:
    def __init__(self, name, lib_card_number):
        self.name = name
        self.lib_card_number = lib_card_number
        self.books = []

    def get_book(self, book, library):
        if library.find_books(title=book.title, author=book.author, year=book.year, available_only=True):
            self.books.append(book)
            book.is_available = False
            return 'Книга получена'
        else:
            return 'Книга недоступна'

    def return_book(self, book, library):
        if book in self.books:
            self.books.remove(book)
            book.is_available = True
            library.add_book(book)
            return 'Книга возвращена'
        else:
            return 'Книга не найдена'

    def __str__(self):
        return f"{self.name} ({self.library_card_number})"


lib = Library()

reader1 = Reader('John', 123)
reader2 = Reader('Sam', 312)

book1 = Book("Война и мир", "Толстой", 1910)
book2 = Book("Отцы и дети", "Тургенев", 1950)

lib.add_reader(reader1)
lib.add_reader(reader2)

lib.add_book(book1)
lib.add_book(book2)

print(lib.find_readers("John"))
# Output: [John Smith (john@example.com, 12345)]

print(lib.find_readers("Sam"))
# Output: [Johnny Smith (john@example.com, 12345)]

print(lib.remove_reader("Sam"))
