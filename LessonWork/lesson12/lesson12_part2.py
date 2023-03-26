# Task 1
# 1.
# with open("lesson.txt") as file:
#     lines = 0
#     for line in file:
#         lines += 1
#     print(lines)

# 2
# line_count = sum(1 for line in open('lesson.txt'))
# print(line_count)


# Task 2
filename = input('Имя файла: ')
try:
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

    str_num = int(input('Номер строки: '))
    new_str = input('Новая строка: ')
    lines[str_num - 1] = new_str + '\n'
    with open(filename, 'w', encoding='utf-8') as file:
        file.readlines(lines)

except FileNotFoundError:
    print('Файла нет')


