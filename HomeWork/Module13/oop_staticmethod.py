# Task 1
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.__numerator = numerator
#         self.__denominator = denominator
#
#     @property
#     def numerator(self):
#         return self.__numerator
#
#     @property
#     def denominator(self):
#         return self.__denominator
#
#     @numerator.setter
#     def set_numerator(self, value):
#         self.__numerator = value
#
#     @denominator.setter
#     def set_denominator(self, value):
#         if value == 0:
#             raise ValueError('Знаменатель не может быть нулем!')
#         self.__denominator = value
#
#     def input_fraction(self):
#         self.numerator = int(input("Введите числитель: "))
#         self.denominator = int(input("Введите знаменатель: "))
#
#     def output_fraction(self):
#         print(f"{self.numerator} / {self.denominator}")
#
#     def adding_fraction(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
#         new_denominator = self.denominator * other_fraction.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def subtract_fraction(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.denominator - self.denominator * other_fraction.numerator
#         new_denominator = self.denominator * other_fraction.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def multiply_fraction(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.numerator
#         new_denominator = self.denominator * other_fraction.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def divide_fraction(self, other_fraction):
#         new_numerator = self.numerator * other_fraction.denominator
#         new_denominator = self.denominator * other_fraction.numerator
#         return Fraction(new_numerator, new_denominator)
#
#
# fr1 = Fraction(10, 15)
# fr2 = Fraction(15, 15)
#
# print('Fraction 1: ')
# fr1.output_fraction()
#
# print('Fraction 2: ')
# fr2.output_fraction()
# print('---' * 5)
# result_addition = fr1.adding_fraction(fr2)
# result_subtraction = fr1.subtract_fraction(fr2)
# result_multiplication = fr1.multiply_fraction(fr2)
# result_division = fr1.divide_fraction(fr2)
#
# # Вывод результатов на экран
# print("Addition:")
# result_addition.output_fraction()
# print()
#
# print("Subtraction:")
# result_subtraction.output_fraction()
# print()
#
# print("Multiplication:")
# result_multiplication.output_fraction()
# print()
#
# print("Division:")
# result_division.output_fraction()
# print()

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
