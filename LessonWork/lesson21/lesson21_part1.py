# import re
#
#
# def analysis_file(filename):
#     text = open(filename, 'r', encoding='utf-8').read()
#     text = file.read()
#     string_count = text.count('\n') + 1
#     words = {}
#     avg_words_len = 0
#     words_list = re.split('[,.!?;\s]', text)
#     for word in words_list:
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1
#
#     avg_words_len = avg_words_len / len(words_list)
#     words_frequency = sorted((word, words[word] / len(words_list)) for word in words)
#     file.close()
#     with open('log.txt', 'w', encoding='utf-8') as f:
#         f.write(f'Кол-во строк: {string_count}')
#     return text
#
#
# print(analysis_file('file.txt'))
from random import randint


# class Vector:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def __str__(self):
#         return f'{Vector.__name__}: ({self.x}, {self.y})'
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, a):
#         return Vector(self.x * a, self.y * a)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __lt__(self, other):
#         return self.x**2 + self.y**2 < other.x**2 + other.y**2
#
#
# vec1 = Vector(2, 5)
# vec2 = Vector(1, 7)
#
# print(vec1 + vec2)
# print(vec1 - vec2)
# print(vec1 * 10)
# print(vec1 == vec2)
# print(vec1 < vec2)


# def retry(max_retries):
#     counter = 0
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             nonlocal counter
#             while counter < max_retries:
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except:
#                     counter += 1
#                     print('Обнаружено ожидание, повторная попытка...')
#         return wrapper
#     return decorator
#
#
# class DatabaseConnetion:
#     @staticmethod
#     @retry
#     def connect():
#         connect = randint(1,100)
#         if connect < 50:
#             print("Connection successful")
#         else:
#             raise Exception
#
#
# connection = DatabaseConnetion()
# connection.connect(5)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Животное издает звук...')
#
#
# class Cat(Animal):
#     def speak(self):
#         Animal.speak(self)
#         print('Мяу')
#
#
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print('Гав')
#
#
# gang = Cat('Муся'), Dog('Шарик')
# for animal in gang:
#     animal.speak()


import datetime


def logger(func):
    def decorator(*args, **kwargs):
        message = f'{datetime.datetime.now()}. Функция вызвана: {func}'
        result = func(*args, **kwargs)
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(message)
            result = func(*args, **kwargs)
            f.write(f'Получился результат: {result}\n')
            return result
    return decorator


