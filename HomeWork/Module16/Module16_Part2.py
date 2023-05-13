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
import logging
import json


class Reader:
    def __init__(self, name, email, library_card_number):
        self.name = name
        self.email = email
        self.library_card_number = library_card_number

    def __str__(self):
        return f"{self.name} ({self.email}, {self.library_card_number})"


class Library:
    def __init__(self):
        self.readers = []
        self.log = logging.getLogger("Library")
        self.log.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.log.addHandler(handler)

    def add_reader(self, name, email, library_card_number):
        reader = Reader(name, email, library_card_number)
        self.readers.append(reader)
        self.log.info(f"Reader {reader} was added")

    def remove_reader(self, email):
        for reader in self.readers:
            if reader.email == email:
                self.readers.remove(reader)
                self.log.info(f"Reader {reader} was removed")
                break

    def update_reader(self, email, name=None, library_card_number=None):
        for reader in self.readers:
            if reader.email == email:
                if name is not None:
                    reader.name = name
                if library_card_number is not None:
                    reader.library_card_number = library_card_number
                self.log.info(f"Reader {reader} was updated")
                break

    def search_readers(self, query):
        results = []
        for reader in self.readers:
            if query in reader.name or query in reader.email or query in reader.library_card_number:
                results.append(reader)
        return results

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            data = {
                "readers": [
                    {"name": reader.name, "email": reader.email, "library_card_number": reader.library_card_number}
                    for reader in self.readers
                ]
            }
            json.dump(data, f)
        self.log.info(f"Library data was saved to {filename}")

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.readers = [
                Reader(reader["name"], reader["email"], reader["library_card_number"])
                for reader in data["readers"]
            ]
        self.log.info(f"Library data was loaded from {filename}")


library = Library()

library.add_reader("John Smith", "john@example.com", "12345")
library.add_reader("Alice Johnson", "alice@example.com", "67890")

print(library.search_readers("John"))
# Output: [John Smith (john@example.com, 12345)]

library.update_reader("john@example.com", name="Johnny Smith")
print(library.search_readers("John"))
# Output: [Johnny Smith (john@example.com, 12345)]

library.remove_reader("alice@example.com")
print(library.search_readers("Alice"))
# Output: []