# while True:
#     figure = input('Введите номер фигуры'
#                    '(1-10, 0 для выхода): ')
#     if figure == 0:
#         break
#     elif figure == '5':
#         size = int(input('Введите размер: '))
#         for i in range(size, 0, -2):
#             print((size - i) // 2 * ' ' + '*' * i +
#                   (size - i) // 2 * ' ')
#         for i in range(2, size + 2, 2):
#             print((size - i) // 2 * ' ' + '*' * i +
#                   (size - i) // 2 * ' ')
#         for i in range(size, -size - 1, -2):
#             if i:
#                 print((size - abs(i)) // 2 * ' * ' + '   ' * abs(i) +
#                       (size - abs(i)) // 2 * ' * ')


# 2^7 - 127 - Standard ASCII
# 2^8 - 255 - Extended ASCII
# 2^31 - UTF("UTF-8" - 8 бит; "UTF-16" - 16 бит...)

# string = 'Hello Женя'
# print(string.encode(encoding='utf-8'))
#
# string = 'Hello'
# print(string)

# string = 'Hello'
# print(string)
# print(string[0])
# print(string[1])
# string = 'Bye'  # Строка - неизменяемый тип данных
# string[0] = 'H'  # Невозможная операция

# string = 'Hello'  # [(0, -5), (1, -4), (2, -3),
# print(string[-1])  # (3, -2), (4, -1)]


# print('Hello' + 'World')
# print('Hello' * 5)

# print(len('Hello'))  # length - c английского "длина"

# my_str = "python was created in the late 1980's " \
#          "by Guido van Rossum."

# print(my_str.capitalize())  # первая буква - заглавная, остальные - строчные
# print(my_str.lower())  # делает все символы строчными
# print(my_str.upper())  # делает все символы заглавными
# print(my_str.title())  # делает первую букву каждого слова заглавной
# print(my_str.swapcase())  # меняет местами строчный и заглавный регистры у всех символов

# my_str = "Python was created in the late 1980's " \
#          "by Guido van Rossum. Python - cool!"

# Ищет подстроку 'Python' в строке my_str
# print(my_str.count('Python'))
# Также поддерживает установку границ поиска
# print(my_str.count('Python', 10, 100))
# print(my_str.count('Python', 10))

# Возвращает индекс начала первого
# вхождения подстроки 'was' в строке my_str
# print(my_str.find('was'))
# print(my_str.find('was', -150, -60))

# Аналогичен find, но бросает исключение, если подстрока не найдена
# print(my_str.index('was'))

# print(my_str.find('Python'))
# Ищут с конца строки
# print(my_str.rfind('Python'))
# print(my_str.rindex('Python'))

# my_str = "Python was created in the late 1980's " \
#          "by Guido van Rossum. Python - cool!"

# Проверяет начало строки на совпадение
# print(my_str.startswith('Py'))
# Также поддерживает кастомные начало и конец проверки
# print(my_str.startswith('Python', 10, 20))

# print(my_str.lower().find('python'))

# Проверяет конец строки на совпадение
# print(my_str.endswith('cool!'))
# Также поддерживает кастомные начало и конец проверки
# print(my_str.endswith('cool!', 10, 20))

# str1 = '123'
# str2 = 'Hello.'
# str3 = 'He11o'
# str4 = '     '
# str5 = '12.3'
# print(str1.isdigit())  # проверяет, что все символы - цифры
# print(str5.isdigit())

# print(str1.isalpha())  # проверяет, что все символы принадлежат алфавиту
# print(str2.isalpha())  # поддерживает любой алфавит

# print(str3.isalnum())  # проверяет, что все символы либо буквы, либо цифры
# print(str2.isalnum())

# print(str1.islower())  # проверяет, что все символы нижние
# print(str1.isupper())  # проверяет, что все символы верхние

# print(str1.istitle())  # проверяет, что все слова начинаются на заглавную букву
# print(str4.isspace())  # проверяет, что строка состоит из пробелов


# string = '   Hello   '

# Центрирует нашу строку, создавая новую указанной длины
# и заполняет пробелы указанным символом
# print(string.center(7, '!'))

# Заменяет табы на пробелы
# print(string.expandtabs(4))

# То же самое, что и center, но по левому и правому краю
# print(string.ljust(10, '#'))
# print(string.rjust(10))

# Убирает пробелы с краев строки
# print(string.strip())

# for i in range(start, end, step):
# Срезы работают примерно, как аргументы range:

# string = 'Hello World'
# print(string[0::4])
# print(string[5:])
# print(string[:5])
#
# Даёт перевернутую копию
# print(string[::-1])

# string = "Hello \nPython"
# print(string)

# print(r'Hello \"safasf\\\ Python')
# name = 'Egor'
# print('Hello {name}. {name} have a nice {day}'.format(name=name, day='evening'))


# print('Result is {0:10.2f}'.format(20.12512512412))

# Практика
# 1.
# print(input('Введите строку')[::-1])


# import string
#
# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.hexdigits)
# print(string.printable)

# 2.
# line = input('Введите строку: ')
#
# count_digits = 0
# count_chars = 0
# for char in line:
#     if char.isdigit():
#         count_digits += 1
#     elif char.isalpha():
#         count_chars += 1
# print(f'Количество букв: {count_chars}')
# print(f'Количество цифр: {count_digits}')


# 3.
# print(input('Введите строку: ').count(
#       input('Введите, что искать: ')))

# Заменяет вхождения подстроки а на подстроку б
# string = 'Hello'
# string = string.replace('World', '#')
# print(string)


# 4.
# print(input('Введите строку: ').replace(
#       input('Введите, что заменить: '),
#       input('Введите, на что заменять: ')))

import string

text = 'повседневная практика показывает, что начало повседневной работы по формированию позиции в значительной ' \
       'степени обуславливает создание всесторонне сбалансированных нововведений. практический опыт ' \
       'показывает, что реализация намеченного плана развития в значительной степени обуславливает ' \
       'создание дальнейших направлений развитая системы массового участия? с другой стороны реализация ' \
       'намеченного плана развития способствует подготовке и реализации'

print('. '.join(map(lambda word: word.capitalize(), text.split('. '))))
print(f'Количество цифр в строке: {len([digit for digit in text if digit.isdigit()])}')
print(f'Количество знаком препинания: {len([j for j in text if j in string.punctuation])}')
print(f'Количество восклицательных знаков: {len([i for i in text if i in "!"])}')
