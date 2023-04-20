# Task 1
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference_length(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.get_circumference_length() == other.get_circumference_length()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.get_circumference_length() < other.get_circumference_length()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.get_circumference_length() > other.get_circumference_length()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.get_circumference_length() <= other.get_circumference_length()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.get_circumference_length() >= other.get_circumference_length()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Circle):
            return self.radius + other.radius
        else:
            return self.radius + other

    def __sub__(self, other):
        if isinstance(other, Circle):
            return self.radius - other.radius
        else:
            return self.radius - other

    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
        else:
            self.radius += other
        return self

    def __isub__(self, other):
        if isinstance(other, Circle):
            self.radius -= other.radius
        else:
            self.radius -= other
        return self

    def __str__(self):
        return f"Окружность с радиусом {self.radius}"


circle1 = Circle(15)
circle2 = Circle(10)


# Проверка равенства радиусов
if circle1 == circle2:
    print("У окружностей одинаковые радиусы.")
else:
    print("У окружностей разные раудиусы.")
print('-----' * 5)


# Сравнение длин
if circle1 < circle2:
    print("Окружность 1 круга меньше, чем окружность 2 круга")
elif circle1 > circle2:
    print("Окружность 1 круга больше, чем окружность 2 круга")
else:
    print("Окружность обоих кругом одинаковая")
print('-----' * 5)


# Процорциональное изменение размеров окружности путем изменения его радиуса
print(circle1 + circle2)
print(circle2 - circle1)

circle1 += 2
print(circle1)

circle2 -= 1
print(circle2)


# Task 2
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator,
                       (self.imag * other.real - self.real * other.imag) / denominator)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


complex1 = Complex(7, 10)
complex2 = Complex(10, 8)

a = complex1 + complex2
print(a)

b = complex1 - complex2
print(b)

c = complex1 * complex2
print(c)

d = complex1 / complex2
print(d)


# Task 3
class Airplane:
    def __init__(self, type: str, passengers: int):
        self.type = type
        self.passengers = passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.type == other.type
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers < other.passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers > other.passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passengers <= other.passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passengers >= other.passengers
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Airplane):
            return self.passengers + other.passengers
        else:
            return self.passengers + other

    def __sub__(self, other):
        if isinstance(other, Airplane):
            return self.passengers - other.passengers
        else:
            return self.passengers - other

    def __iadd__(self, other):
        if isinstance(other, Airplane):
            self.passengers += other.passengers
        else:
            self.passengers += other
        return self

    def __isub__(self, other):
        if isinstance(other, Airplane):
            self.passengers -= other.passengers
        else:
            self.passengers -= other
        return self

    def __str__(self):
        return f"Самолет типа: {self.type} с {self.passengers} пассажиром(ами) на борту"


airplane1 = Airplane('Истребитель', 2)
airplane2 = Airplane('Лайнер', 100)


# Проверка равенства типов самолетов
if airplane1 == airplane2:
    print("Тип самолетов идентичен.")
else:
    print("Самолеты имеют разный тип.")
print('-----' * 5)


# Сравнение самолетов по макс. кол-ву пассажиров на борту
if airplane1 < airplane2:
    print("Кол-во пассажиров на борту 1 самолета меньше, чем на 2")
elif airplane1 > airplane2:
    print("Кол-во пассажиров на борту 1 самолета больше, чем на 2")
else:
    print("Кол-во пасаажиров на борту одинаково")
print('-----' * 5)


# Увеличение/уменьшение пассажиров в самолете
print(airplane1 + airplane2)
print(airplane2 - airplane1)

airplane1 += 2
print(airplane1)

airplane2 -= 1
print(airplane2)


# Task 4
class Flat:
    def __init__(self, area: int, price: int):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __repr__(self):
        return f"Квартира площадью {self.area} стоит {self.price}"


flat1 = Flat(120, 12000000)
flat2 = Flat(50, 3000000)


#Проверка равенства площадей квартир
if flat1 == flat2:
    print("Площади квартир идентичны.")
else:
    print("Квартиры имеют разные площади.")
print('-----' * 5)


# Сравнение цен на квартиры
if flat1 < flat2:
    print("Цена на 1 квартиру ниже, чем на 2")
elif flat1 > flat2:
    print("Цена на 1 квартиру выше, чем на 2")
else:
    print("Цены на квартиры одинаковые")
