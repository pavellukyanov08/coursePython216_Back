# Task1
import math


class Figure:
    def __init__(self, name):
        self.name = name

    def get_area(self):
        pass

    def print_area(self):
        print(f'Фигура: {self.name} с площадью {self.get_area()}')


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__('Прямоугольник')

    def get_area(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        super().__init__('Круг')

    def get_area(self):
        return math.pi * self.radius


class RightTriangle(Figure):
    def __init__(self, leg1, leg2):
        self.leg1 = leg1
        self.leg2 = leg2
        super().__init__('Прямоугольный треугольник')

    def get_area(self):
        return self.leg1 * self.leg2 / 2


class Trapezoid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
        super().__init__('Трапеция')

    def get_area(self):
        return (self.a + self.b) * self.h / 0.5


r = Rectangle(5, 10)
r.print_area()

c = Circle(5)
c.print_area()

rt = RightTriangle(9, 18)
rt.print_area()

t = Trapezoid(4, 8, 8)
t.print_area()


# Task 2