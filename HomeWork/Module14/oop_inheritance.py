import math
# Task1
#
#
# class Figure:
#     def __init__(self, name):
#         self.name = name
#
#     def get_area(self):
#         pass
#
#     def print_area(self):
#         print(f'Фигура: {self.name} с площадью {self.get_area()}')
#
#
# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         super().__init__('Прямоугольник')
#
#     def get_area(self):
#         return self.a * self.b
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#         super().__init__('Круг')
#
#     def get_area(self):
#         return math.pi * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     def __init__(self, leg1, leg2):
#         self.leg1 = leg1
#         self.leg2 = leg2
#         super().__init__('Прямоугольный треугольник')
#
#     def get_area(self):
#         return self.leg1 * self.leg2 / 2
#
#
# class Trapezoid(Figure):
#     def __init__(self, a, b, h):
#         self.a = a
#         self.b = b
#         self.h = h
#         super().__init__('Трапеция')
#
#     def get_area(self):
#         return (self.a + self.b) * self.h / 0.5
#
#
# r = Rectangle(5, 10)
# r.print_area()
#
# c = Circle(5)
# c.print_area()
#
# rt = RightTriangle(9, 18)
# rt.print_area()
#
# t = Trapezoid(4, 8, 8)
# t.print_area()


# Task 2
# class Figure:
#     def area(self):
#         pass
#
#     def __int__(self):
#         return int(self.area())
#
#     def __str__(self):
#         return f"Фигура с площадью {self.area()}"
#
#
# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def __str__(self):
#         return f"Прямоугольник с площадью {self.area()}"
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def __str__(self):
#         return f"Круг с площадью {self.area()}"
#
#
# class RightTriangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return 0.5 * self.a * self.b
#
#     def __str__(self):
#         return f"Прямоугольный треугольник с площадью {self.area()}"
#
#
# class Trapezium(Figure):
#     def __init__(self, a, b, h):
#         self.a = a
#         self.b = b
#         self.h = h
#
#     def area(self):
#         return 0.5 * (self.a + self.b) * self.h
#
#     def __str__(self):
#         return f"Трапеция с площадью {self.area()}"
#
#
# r = Rectangle(5, 10)
# print(int(r))
# print(str(r))
#
# c = Circle(4)
# print(int(c))
# print(str(c))
#
# rt = RightTriangle(3, 6)
# print(int(rt))
# print(str(rt))
#
# tr = Trapezium(5, 10, 4)
# print(int(tr))
# print(str(tr))


# Task 3
import pickle


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'Координаты: ({self.x}, {self.y})')

    def save(self, file_name):
        with open(file=file_name, mode='wb') as f:
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
        print(f'Квадрат: Координаты ({self.x}, {self.y}), Длина: {self.length}')


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f'Прямоугольник: Координаты ({self.x}, {self.y}), Ширина: {self.width}, Высота: {self.height}')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        print(f'Круг: Координаты ({self.x}, {self.y}), Радиус: {self.radius}')


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        print(f'Елипс: Координаты ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}')


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
