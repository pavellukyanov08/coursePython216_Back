# class A:
#     def __init__(self):
#         self.value = 3
#
#     def print_a_value(self):
#         print(self.a)
#
#
# class B:
#     def __init__(self):
#         self.b = 5
#
#     def print_b_value(self):
#         print(self.b)
#
#
# class C(B, A):
#     pass
#
#
# a = C()
# a.print_b_value()
# import math
#
#
# # Task 1
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     @property
#     def area(self):
#         return math.pi * self.__radius ** 2
#
#
# class Square:
#     def __init__(self, side_length):
#         self.__side_length = side_length
#
#     @property
#     def area(self):
#         return self.__side_length ** 2
#
#
# class CircleInSquare(Circle, Square):
#     def __init__(self, side_length, radius):
#
#         self.side_length = side_length
#         self.radius = radius
#         if self.radius > self.side_length / 2:
#             raise ValueError("Круг слишком велик, чтобы поместиться в квадрат")
#
#     def circle_in_square(self):
#         return self.side_length ** 2 - math.pi * (self.radius ** 2)
#
#
# c = Circle(10)
# s = Square(5)
# cIs = CircleInSquare(10, 2)
# print(cIs.circle_in_square())


# Task 2
class Body:
    def __init__(self, type_bd):
        self.__type_bd = type_bd

    @property
    def type_body(self):
        return self.__type_bd


class Wheels:
    def __init__(self, disk_size):
        self.__disk_size = disk_size

    @property
    def disk_size(self):
        return self.__disk_size


class Engine:
    def __init__(self, capacity):
        self.__capacity = capacity

    @property
    def engine_capacity(self):
        return self.__capacity


class Car(Body, Wheels, Engine):
    def __init__(self, type_bd, disk_size, capacity):
        Body.__init__(self, type_bd)
        Wheels.__init__(self, disk_size)
        Engine.__init__(self, capacity)

    def output_info(self):
        return f'Автомобиль:\n   ' \
               f'кузов: {self.type_body};\n   ' \
               f'размер дисков: {self.disk_size};\n   ' \
               f'объем двигателя: {self.engine_capacity}'


car = Car('Хэтчбек', 22, 1.6)
print(car.output_info())


# Task 3
# class Animal:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def show(self):
#         print('Имя:', self.name)
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, breed)
#
#     def sound(self):
#         print('Гав')
#
#     def sound(self):
#         print('Гав')
#
#     def breed_type(self):
#         print("Порода:", self.breed, "(Собака)")
#
#
# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, breed)
#
#     def sound(self):
#         print("Мяу")
#
#     def breed_type(self):
#         print("Порода:", self.breed, "(Кошка)")
#
#
# dog = Dog("Тузик", "Лайка")
# cat = Cat("Гаражик", "Мейн-кун")
#
# dog.sound()
# dog.show()
# dog.breed_type()
#
# cat.sound()
# cat.show()
# cat.breed_type()
