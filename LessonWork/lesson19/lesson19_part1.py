# SOLID - пять основных принципов дизайна создания классовой архитектуры
# 1. S - Single Responsibitity
# Принцип единственной ответственности - у объекта экземпляра класса
# должна быть только одна обязанность, решение которой
# полностью входит в тело класса

# class UserAccount:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# class UserDB:
#     def __init__(self, id):
#         self.id = id
#
#     def get_name(self):
#         pass


# 2. - Open - Closed
# Принцип открытости/закрытости - программируемые сущности (классы, функции, модели) должны быть открыты для
# расширения, но закрыты для изменений.

class DiscountVIP:
    def __init__(self, price):
        self.price = price

    def give_discount(self, buyer):
        if buyer == 'vip':
            return self.price * 0.9
        elif buyer == 'favorite':
            return self.price * 0.8


# class DiscountFAV(DiscountVIP):
#     def give_discount(self):
#         return self.price * 0.8


# 3. L - Liskov Substitution Principle
# Принцип подстановки Барбары Лисков - сущности, которые используют базовый тип данных,
# должны иметь возможность
# использовать подтипы базового типа, не зная об этом

# class IntegerNumber:
#     def __init__(self, value):
#         self.value = int(value)
#
#     def __str__(self):
#         return f'{self.value}'
#
# def multiplay_string(string: str, num: IntegerNumber):
#     try:
#         return string * num.value
#     except TypeError as e:
#         if 'float' in repr(e):
#             return string * int(num.value)
#
#
# class FloatNumber(IntegerNumber):
#     def __init__(self, value):
#         self.value = value
#
#
# a = IntegerNumber(5.5)
# b = FloatNumber(5.5)
# print(multiplay_string('Hi ', a))
# print(multiplay_string('Hi ', b))


# 4. I - Interface Substitution Principle
# Принцип разделения интерфейса - клиенты не должны зависеть от
# функций, которые они не используют
# from abc import ABC, abstractmethod
#
#
# class CallingDevice(ABC):
#     @abstractmethod
#     def make_call(self):
#         pass
#
#
# class MessagingDevice(ABC):
#     @abstractmethod
#     def send_message(self):
#         pass
#
#
# class InternetBrowsingDevice(ABC):
#     @abstractmethod
#     def browse_internet(self):
#         pass
#
#
# class SmartPhone(MessagingDevice, CallingDevice, InternetBrowsingDevice):
#     def make_call(self):
#         pass
#
#     def send_message(self):
#         pass
#
#     def browse_internet(self):
#         pass
#
#
# class OldPhone(MessagingDevice, CallingDevice):
#     def make_call(self):
#         pass
#
#     def send_message(self):
#         pass


# 5. D - Dependency Inversion Principle
# Принцип инверсии зависимостей модули верхних уровней
# не должны зависеть от модулей нижних уровней. А оба
# типа модулей должны зависеть от абстракций. Cами абстракции
# не должны зависеть от деталей реализации, а детали реализаций
# должны зависеть от абстракций.


# class Payment:
#     def do_transaction(self, amount):
#         pass
#
#
# class Cash(Payment):
#     def pay(self, amount):
#         pass
#
#
# class Shop:
#     @staticmethod
#     def do_payment(payment, amount):
#         payment.do_transaction(amount)


# Task
# class Pasta:
#     def choose_recipe(self):
#         pass
#
#     def make_recipe

#     def __init__(self):
#         self.type = None
#         self.sauce = None
#         self.fillings = []
#         self.add_ons = []
#
#     def __str__(self):
#         return f"Паста: ({self.type} c соусом {self.sauce}, " \
#                f"начинкой {', '.join(self.fillings)} и добавками {', '.join(self.add_ons)})"
#
#     def add_filling(self, filling):
#         self.fillings.append(filling)
#
#     def add_add_on(self, add_on):
#         self.add_ons.append(add_on)
#         return self
#
#
# class BucatiniBuilder:
#     def __init__(self):
#         self.pasta = Pasta()
#         self.pasta.type = 'Букатини'
#
#     def add_sauce(self, sauce):
#         self.pasta.sauce = sauce
#         return self
#
#
# class CannelloniBuilder:
#     def __init__(self):
#         self.pasta = Pasta()
#         self.pasta.type = 'Каннеллони'
#
#     def add_sauce(self, sauce):
#         self.pasta.sauce = sauce
#         return self
#
#
# class PastaCreator:
#     def __init__(self, builder):
#         self.builder = builder
#
#     def make_pasta(self, sauce, fillings=[], add_ons=[]):
#         self.builder.add_sauce(sauce)
#         for filling in fillings:
#             self.builder.pasta.add_filling(filling)
#         for add_on in add_ons:
#             self.builder.pasta.add_add_on(add_on)
#
#         return self.builder.pasta
#
#
# bucatini = BucatiniBuilder()
#
# creator = PastaCreator(bucatini)
# pasta1 = creator.make_pasta('Сырный', ["Мясной", "Грибной"], ["Пармезан", "Чеснок"])
#
# сannelloni = CannelloniBuilder()
#
# creator = PastaCreator(сannelloni)
# pasta2 = creator.make_pasta('Сырный', ["Сырной", "Томатной"], ["Пармезан", "Чеснок"])
#
# print(pasta1)
# print(pasta2)