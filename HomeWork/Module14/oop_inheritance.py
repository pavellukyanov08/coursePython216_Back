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
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        info = ''
        info += f'{self.__class__.__name__}:\n'
        for key, value in self.__dict__.items():
            info += f'\t{key}: {value}\n'
        return info

    def save(self, filename='shape.txt'):
        try:
            Shape.load(filename)
        except Exception:
            open(filename, 'w')
        with open(filename, 'a') as f:
            f.write(f'{self.__class__.__name__}(**{self.__dict__})\n')

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            if len(lines) == 1:
                return eval(lines[0])
            else:
                return list(map(eval, lines))

    def __str__(self):
        return self.show()


class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height


shapes = [
    Circle(10, 10, 5),
    Square(20, 20, 10),
    Rectangle(30, 30, 5, 7),
    Ellipse(40, 40, 7, 5)
]

for shape in shapes:
    shape.save('shape.txt')

new_shapes = Shape.load('shape.txt')
for shape in new_shapes:
    shape.show()


