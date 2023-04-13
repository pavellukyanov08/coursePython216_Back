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