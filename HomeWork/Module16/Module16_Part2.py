# # Task 1
from abc import ABC, abstractmethod
#
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


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)


class Calculator:
    def __init__(self):
        self._current = 0

    def add(self, value):
        self._current += value

    def sub(self, value):
        self._current -= value

    def mult(self, value):
        self._current *= value

    def div(self, value):
        self._current /= value

    def get_current_value(self):
        return self._current


class AddCommand:
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.add(self.value)


class SubCommand:
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.sub(self.value)


class MultCommand:
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.sub(self.value)


class DivCommand:
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.sub(self.value)


calc = Calculator()

commands = [
    AddCommand(calc, 10),
    SubCommand(calc, 7),
    SubCommand(calc, 5),
    DivCommand(calc, 12),
    PrintCommand(calc.get_current_value())
]

for command in commands:
    command.execute()

print("Final value:", calc.get_current_value())
