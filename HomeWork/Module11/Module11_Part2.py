# Task 1
# with open(file='file1.txt', mode='r', encoding='utf-8') as file1, \
#         open(file='file2.txt', mode='r', encoding='utf-8') as file2:
#     line1 = file1.readlines()
#     line2 = file2.readlines()
#
# for i, (line1, line2) in enumerate(zip(line1, line2)):
#     if line1 != line2:
#         print(f"Строка {i+1}: {line1.strip()} (из первого файла) не совпадает с {line2.strip()} (из второго файла)")


# Task 2
# with open(file='file1.txt', mode='r', encoding='utf-8') as file1, \
#         open(file='file2.txt', mode='w', encoding='utf-8') as file2:
#     content = file1.read()
#
#     count_chars = len(content)
#     count_lines = content.count('\n') + 1
#     count_vowels = sum([1 for char in content if char in 'aeiouyAEIOUY'])
#     count_consonant = sum([1 for char in content if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'])
#     count_digit = sum([1 for char in content if char in '0123456789'])
#
#     file2.write(f'Символов: {str(count_chars)}; \nСтрок: {count_lines}; \nГласных: {count_vowels}; \nСогласных:'
#                 f' {count_consonant}; \nЦифр: {count_digit}')


# Task 3
# with open("file1.txt", "r") as file1:
#     lines = file1.readlines()
#
# with open("file2.txt", "w") as file2:
#     file2.writelines(lines[:-1])


# Task 4
# with open(file='file1.txt', mode='r', encoding='utf-8') as file:
#     min_length = 0
#     min_line = ''
#
#     for line in file:
#         length = len(line.strip())
#         if length < min_length:
#             min_length = length
#             min_line = line.strip()
#
# print(f'Самая длинная строка: {min_line}, ее длина: {min_length}')


# Task 5
# with open(file='file1.txt', mode='r', encoding='utf-8') as file:
#     content = file.read()
#     count_word = content.count(input('Введите слово: '))
#     print(count_word)


# Task 6
# with open(file='file1.txt', mode='r+', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
#
#     search_word = input('Искомое слово: ')
#     if search_word in content:
#         replace_word = input('Новое слово: ')
#         content = content.replace(search_word, replace_word)
#         print(f'Замена успешна!. \nНовые данные: {content}')
#     else:
#         print('Искомое слово не найдено')
#
#     file.seek(0)
#     file.write(content)
#     file.truncate()
