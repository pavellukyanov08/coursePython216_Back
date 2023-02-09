# import webbrowser as wb, cowsay as cw, time
#
# user_say = input('Enter some word: ')
#
# if user_say == 'Христос Воскрес':
#     print('3...')
#     time.sleep(1)
#     print('2...')
#     time.sleep(1)
#     print('1...')
#     time.sleep(1)
#     cw.cow('Ну... Понеслась...')
#     wb.open('https://www.youtube.com/watch?v=Xv-kQqgE5HE&ab_channel=popugzaputina')

# class People:
#     def __int__(self, name, age, sex, isMarried):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.isMarried = isMarried
#
#     def first_people(self):
#         print('Имя:', self.name, '; возраст:', self.age, '; пол:', self.sex, '; статус:', self.isMarried)
#
#
# people1 = People('John', 21, 'male', True)
# people2 = People('Sarah', 25, 'female', False)
#
# people1.first_people()
# class People:
#     def __init__(self, name=None, age=None, sex=None, isMarried=None):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.isMarried = isMarried
#
#     def first_people(self):
#         print(f'Имя: {self.name}; возраст: {self.age}; пол: {self.sex}; статус: {self.isMarried}')
#
# people1 = People('John', 25, 'male', True)
# people2 = People('Sarah', 20, 'female', False)
#
# people1.first_people()
# people2.first_people()


import re

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
print(match[0] if match else 'Not found', '\n') # -> 23-12


match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
print(match[0] if match else 'Not found', '\n') # -> Not found


match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
print('YES' if match else 'NO', '\n') # -> YES


match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
print('YES' if match else 'NO', '\n') # -> NO


print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'), '\n')
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']


print(re.findall(r'\d\d\.\d\d\.\d{4}',
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'), '\n')
# -> ['19.01.2018', '01.09.2017']


for m in re.finditer(r'\d\d\.\d\d\.\d{4}',
                     r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
    print('Дата', m[0], 'начинается с позиции', m.start(), '\n')
# -> Дата 19.01.2018 начинается с позиции 20
# -> Дата 01.09.2017 начинается с позиции 45


print(re.sub(r'\d\d\.\d\d\.\d{4}',
             r'DD.MM.YYYY',
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY
