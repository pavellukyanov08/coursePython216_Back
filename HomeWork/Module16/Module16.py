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
