# Task 1
class Fraction:
    # counter = 0

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        # Fraction.counter += 1

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError('Знаменатель не может быть нулем!')
        self.__denominator = value

    def output_fraction(self):
        print(f"{self.numerator} / {self.denominator}")

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def counter():
        print(f'counter = {Fraction.counter}')


fr1 = Fraction(10, 15)
fr2 = Fraction(15, 15)

result_addition = fr1.__add__(fr2)
result_subtraction = fr1.__sub__(fr2)
result_multiplication = fr1.__mul__(fr2)
result_division = fr1.__truediv__(fr2)

print("Addition:")
result_addition.output_fraction()
print()

print("Subtraction:")
result_subtraction.output_fraction()
print()

print("Multiplication:")
result_multiplication.output_fraction()
print()

print("Division:")
result_division.output_fraction()
print()

# Fraction.counter()


# Task 2
# class Temperature:
#     counter = 0
#
#     @staticmethod
#     def convert_to_celsius(fahrenheit_temp):
#         Temperature.counter += 1
#         return (fahrenheit_temp - 32) / 1.8
#
#     @staticmethod
#     def convert_to_fahrenheit(celsius_temp):
#         Temperature.counter += 1
#         return celsius_temp * 1.8 + 32
#
#     @staticmethod
#     def counts_number():
#         return Temperature.counter
#
#
# t = Temperature()
# print(f'Температура из Фаренгейта в Цельсий: {t.convert_to_celsius(50)}')
# print(f'Температура из Цельсия в Фаренгейт: {t.convert_to_fahrenheit(109)}')
# print(f'Количество подсчетов: {t.counts_number()}')


# Task 3
# class Measures:
#     @staticmethod
#     def convert_to_metric(inches, foot, yard):
#         # перевод из дюймов в сантиметры, из футов в метры, из ярдов в метры
#         return inches * 2.539, foot * 0.3048, yard * 0.9144
#
#     @staticmethod
#     def convert_to_eng(meters, centimeters):
#         # перевод из метров в ярды, из сантиметров в дюймы, из метров в ярды
#         return meters * 1.094, centimeters * 0.3937, meters * 1.094
#
#
# m = Measures()
# print(f'Перевод из дюймов в сантиметры, из футов в метры, из ярдов в метры: {m.convert_to_metric(16, 10, 15)}')
# print(f'Перевод из метров в ярды, из сантиметров в дюймы, из метров в ярды: {m.convert_to_eng(100, 40)}')
