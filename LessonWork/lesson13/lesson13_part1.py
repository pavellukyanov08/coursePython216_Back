import re

# 1.

# string = 'A book is wet'
# result = re.search('[euioa].*[qwrtypsdfghjklzxcvbnm]', string, flags=re.IGNORECASE)
# print(result)

# 2.

# string = 'https://www.google.com/search?q=main&oq=aqs=chrome..69i57j69i60l3.508j0j7&sourceid=chrome&ie=UTF-8'
# result = re.fullmatch('https://[^\s]+\.[a-z]{2,6}[^\s]+', string)
# print(result, len(string))

# 3.

# string = 'a Book is wet'
# result = re.fullmatch(r".*\b[A-ZА-ЯЁ].*", string)
# print(result)

# 4.

# string = 'book letter world hello nope'
# result = re.finditer(r'\b\w*(\w)\1\w*', string)
# for i in result:
#     print(i)


# --------------------Файлы----------------------
# 1.

# text_file = 'numbers.txt'
# banned_words_file = 'words.txt'
# cleared_text_file = 'out.txt'
# with open(text_file, 'r') as text, open(banned_words_file, 'r') as words:
#     text = text.read()
#     words = re.split('[,.!?\s]+', words.read())
#     for word in words:
#         text = text.replace(word, '')
# with open(cleared_text_file, 'w') as out:
#     out.write(text)


# 2.

# translit_dict = {'ы': 'y', 'ь': "'", 'ъ': "''",
#                  'А': 'A', 'а': 'a',
#                  'Б': 'B', 'б': 'b',
#                  'В': 'V', 'в': 'v',
#                  'Г': 'G', 'г': 'g',
#                  'Д': 'D', 'д': 'd',
#                  'Е': 'Ye', 'е': 'ye',
#                  'Ж': 'Zh', 'ж': 'zh',
#                  'З': 'Z', 'з': 'z',
#                  'И': 'I', 'и': 'i',
#                  'Й': 'Y', 'й': 'y',
#                  'К': 'K', 'к': 'k',
#                  'Л': 'L', 'л': 'l',
#                  'М': 'M', 'м': 'm',
#                  'Н': 'N', 'н': 'n',
#                  'О': 'O', 'о': 'o',
#                  'П': 'P', 'п': 'p',
#                  'Р': 'R', 'р': 'r',
#                  'С': 'S', 'с': 's',
#                  'Т': 'T', 'т': 't',
#                  'У': 'U', 'у': 'u',
#                  'Ф': 'F', 'ф': 'f',
#                  'Х': 'Kh', 'х': 'kh',
#                  'Ц': 'Ts', 'ц': 'ts',
#                  'Ч': 'Ch', 'ч': 'ch',
#                  'Ш': 'Sh', 'ш': 'sh',
#                  'Щ': 'Shch', 'щ': 'shch',
#                  'Э': 'E', 'э': 'e',
#                  'Ю': 'Yu', 'ю': 'yu',
#                  'Я': 'Ya', 'я': 'ya',
#                  }
#
#
# def translit(langs, input_file, output_file):
#     in_text = open(input_file, 'r', encoding='utf-8').read()
#     if langs == ['ru', 'en']:
#         for key, value in translit_dict.items():
#             in_text = in_text.replace(key, value)
#     elif langs == ['en', 'ru']:
#         for key, value in translit_dict.items():
#             in_text = in_text.replace(value, key)
#     else:
#         print('Такие языки не поддерживаются данной программой!')
#     out_file = open(output_file, 'w', encoding='utf-8')
#     out_file.write(in_text)
#     out_file.close()
#
#
# input_file = input('Введите имя исходного файла: ')
# translit_langs = input('Введите, из какого в какой язык транслитерировать:\n'
#                        'Пример: en -> ru\n')
# output_file = input('Введите имя файла, в который сохранить перевод: ')
# translit(translit_langs.split(' -> '), input_file, output_file)


# 3.

# def merge_files(input_filenames, output_filename):
#     with open(output_filename, 'w', encoding='utf-8') as output_file:
#         for input_filename in input_filenames:
#             with open(input_filename, 'r', encoding='utf-8') as input_file:
#                 output_file.write(input_file.read())
#
#
# input_filenames = []
# while True:
#     filename = input('Enter a filename (or "quit" to finish): ')
#     if filename == 'quit':
#         break
#     input_filenames.append(filename)
#
#
# output_filename = input('Enter the output filename: ')
# merge_files(input_filenames, output_filename)


# 4.

# def merge_common_symbols(input_filenames, output_filename):
#     with open(output_filename, 'w', encoding='utf-8') as output_file:
#         first = True
#         symbols = set()
#         for input_filename in input_filenames:
#             with open(input_filename, 'r', encoding='utf-8') as input_file:
#                 if first:
#                     symbols = set(input_file.read())
#                     first = False
#                 else:
#                     symbols = symbols.intersection(input_file.read())
#         output_file.write(''.join(symbols))
#
#
# input_filenames = []
# while True:
#     filename = input('Enter a filename (or "quit" to finish): ')
#     if filename == 'quit':
#         break
#     input_filenames.append(filename)
# output_filename = input('Enter the output filename: ')
# merge_common_symbols(input_filenames, output_filename)
