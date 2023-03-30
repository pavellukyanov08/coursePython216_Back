# Task 1
import re

# string = 'Apple veritus percipit'
# match = re.findall('^[aeiouyAEIOUY].*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$', string)
# print(match)


# Task 2
# url_regex = re.compile(
#     r'^(?:http|ftp)s?://'  # протокол
#     r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # доменное имя
#     r'localhost|'  # localhost
#     r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP-адрес
#     r'(?::\d+)?'  # порт
#     r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # путь
# # Пример использования:
# url = 'https://www.example.com/path/to/file.html?param=value'
# if url_regex.match(url):
#     print('Ссылка введена корректно')
# else:
#     print('Ссылка введена некорректно')


# Task 3
# text = 'Hello world! This is a Test string.'
# matches = re.findall(r'[A-Z][a-zA-Z]*', text)
# print(matches)


# Task 4
# text = 'The book is on the shelf. Letter to the editor.'
# matches = re.findall(r'(\w)\1', text)
# print(matches)