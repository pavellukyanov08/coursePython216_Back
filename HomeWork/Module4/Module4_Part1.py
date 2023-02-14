# Task 1
# string = input('Введите строку: ')
#
# string = string.lower()
#
# forbidden = ('.', '?', '!', ':', ';', '-', '—', ' ', ',')
# text = ''.join(symbol for symbol in string if symbol not in forbidden)
#
# if text == text[::-1]:
#     print('Слово палиндром')
# else:
#     print('Слово не палиндром')


# Task 2
# text = input('Введите текст: ')
# words = input('Введите слова: ')
#
# for words in words.split():
#     text = text.replace(words, words.upper())
# print(f'Измененный текст: {text}')


# Task 3
# import re
#
# text = input("Введите какой-то текст: ")
#
# сделано с помощью регулярок
# re_text = re.sub(r'[.!?]\s', r'.', text)
# sentences_count = len(re_text.split('.'))
# print(f'Количество предложений в тексте равно: {sentences_count} .')
