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
# import copy
#
#
# class Prototype:
#     def __init__(self):
#         self._objects = {}
#
#     def register_object(self, model, obj):
#         self._objects[model] = obj
#
#     def clone(self, model, **kwargs):
#         obj = copy.deepcopy(self._objects.get(model))
#         obj.__dict__.update(kwargs)
#         return obj
#
#
# class Car:
#     def __init__(self):
#         self._model = None
#         self._year = None
#         self._color = None
#
#     def __str__(self):
#         return f"{self._model} ({self._year} {self._color})"
#
#     def set_model(self, model):
#         self._model = model
#
#     def set_year(self, year):
#         self._year = year
#
#     def set_color(self, color):
#         self._color = color
#
#
# car_prototype = Prototype()
# car = Car()
# car.set_model("Tesla")
# car.set_year(2015)
# car.set_color("red")
# car_prototype.register_object("red_tesla", car)
#
# # создаем копию объекта
# new_car = car_prototype.clone("red_tesla")
# print(new_car)  # Tesla (red)
#
# # изменяем атрибуты копии объекта
# new_car.set_model("BMW")
# new_car.set_year(2020)
# new_car.set_color("blue")
# print(new_car)  # BMW (blue)

