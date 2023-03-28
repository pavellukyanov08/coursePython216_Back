import re

# name = input('Введите имя: ')
# result = re.search('Саша', name)
#
# print(result.start())

# name = input('Введите число из 1: ')
# result = re.search('1{3}', name)
# print(result)

text = ['123456@i.ru', '123_456@ru.name.ru', 'login@i.ru', 'norwH-1@i.ru', 'login.3@i.ru', 'Login.3-67@i.ru',
        '1login@ru.name.ru']
result = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(result)
