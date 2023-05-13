# Task 1
# class Car:
#     def __init__(self):
#         self.model = ''
#         self.eng = ''
#         self.color = ''
#         self.cruise_control = False
#         self.door_closers = False
#         self.smart_access = False
#
#     def __str__(self):
#         return f"Модель: ({self.model}, " \
#                f"\n engine: {self.eng}, " \
#                f"\n color: {self.color}, " \
#                f"\n cruise_control: {self.cruise_control}, " \
#                f"\n doors_closers: {self.door_closers}, " \
#                f"\n smart access: {self.smart_access})\n"
#
#
# class BMWBuilder:
#     def __init__(self, model, eng, color):
#         self.car = Car()
#         self.car.model = model
#         self.car.eng = eng
#         self.car.color = color
#
#     def add_closers(self):
#         self.car.door_closers = False
#         return self
#
#     def add_cruise(self):
#         self.car.cruise_control = True
#         return self
#
#     def add_access(self):
#         self.car.smart_access = True
#         return self
#
#     def build(self):
#         return self.car
#
#
# class ToyotaBuilder:
#     def __init__(self, model, eng, color):
#         self.car = Car()
#         self.car.model = model
#         self.car.eng = eng
#         self.car.color = color
#
#     def add_closers(self):
#         self.car.door_closers = False
#         return self
#
#     def add_cruise(self):
#         self.car.cruise_control = True
#         return self
#
#     def add_access(self):
#         self.car.smart_access = False
#         return self
#
#     def build(self):
#         return self.car
#
#
# bmw_build = BMWBuilder('BMW M5', '4.4l 625hp', 'white')
# bmw_build.add_closers()
# bmw_build.add_access()
# bmw_build.build()
#
#
# toyota_build = ToyotaBuilder('Toyota Camry', '3.2l 350hp', 'black')
# toyota_build.add_closers()
# toyota_build.add_access()
# toyota_build.build()
#
# print(bmw_build.build())
# print(toyota_build.build())


# Task 2
# class Pasta:
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


# Task 3
from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Car(Prototype):
    def __init__(self, mode, color, engine):
        self.model = mode
        self.color = color
        self.engine = engine

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f'{self.model} (color: {self.color},  engine: {self.engine})'


car1 = Car('BMW M5', 'white', '4.4l')
car2 = car1.clone()

print(f'Первый объект: {car1}')
print(f'Копия первого объекта: {car2}')
print('----'*5)

car2.model = 'Toyota Camry'
car2.engine = '3.2l'

print(f'Измененная копия первого объекта: {car2}')
