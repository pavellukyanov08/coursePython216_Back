# from abc import ABC, abstractmethod
# import math
# Task1
#
#
# class Figure(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     def __int__(self):
#         return int(self.get_area)
#
#     def __str__(self):
#         return f"Фигура с площадью {self.get_area}"
#
#
# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property
#     def get_area(self):
#         return self.a * self.b
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def get_area(self):
#         return math.pi * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     def __init__(self, leg1, leg2):
#         self.leg1 = leg1
#         self.leg2 = leg2
#
#     @property
#     def get_area(self):
#         return self.leg1 * self.leg2 / 2
#
#
# class Trapezoid(Figure):
#     def __init__(self, a, b, h):
#         self.a = a
#         self.b = b
#         self.h = h
#
#     @property
#     def get_area(self):
#         return (self.a + self.b) * self.h / 0.5
#
#
# r = Rectangle(5, 10)
# c = Circle(5)
# rt = RightTriangle(9, 18)
# t = Trapezoid(4, 8, 8)
#
# shapes = {r, c, rt, t}
# for shape in shapes:
#     print(shape.get_area)
#     print(int(shape))
#     print(shape)


# Task 3
import pickle


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты: ({self.x}, {self.y})")

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)
        print("Фигура сохранена в файл: ", file_name)

    @staticmethod
    def load(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)


class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length

    def show(self):
        print(f"Квадрат: ({self.x}, {self.y}), Длина: {self.length}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f"Треугольник: ({self.x}, {self.y}), Ширина: {self.width}, Высота: {self.height}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        print(f"Круг: ({self.x}, {self.y}), Радиус: {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f"Эпипс: ({self.x}, {self.y}), Ширина: {self.width}, Высота: {self.height}")


# Создаем список фигур
shapes = [
    Square(0, 0, 5),
    Rectangle(10, 10, 20, 30),
    Circle(50, 50, 10),
    Ellipse(100, 100, 30, 50)
]

# Сохраняем фигуры в файл
for i, shape in enumerate(shapes):
    file_name = f"shape{i}.txt"
    shape.save(file_name)

# Загружаем фигуры из файла в другой список
loaded_shapes = []
for i in range(len(shapes)):
    file_name = f"shape{i}.txt"
    loaded_shapes.append(Shape.load(file_name))

# Выводим информацию о каждой из фигур
for shape in loaded_shapes:
    shape.show()



