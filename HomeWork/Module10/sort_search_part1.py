# Task 1
# from random import randint
#
# nums_list = [randint(1, 20) for _ in range(9)]
# print('Исходный список:', nums_list)
#
# n = len(nums_list)
# arith_mean = sum(nums_list) / n
#
# if arith_mean > 0:
#     two_thirds = int(n * 2 / 3)
#     sorted_nums = sorted(nums_list[:two_thirds])
#     print('Сортировка две трети списка:', sorted_nums)
# else:
#     first_thirds = int(n / 3)
#     sorted_nums = sorted(nums_list[:first_thirds])
#     print('Сортировка первой трети списка:', sorted_nums)
#
# unsorted_nums = nums_list[two_thirds:]
# reverse_nums = unsorted_nums[::-1]
#
# print('Вывод сортированной части + перевернутой:', sorted_nums + reverse_nums)

# Task 2
from random import randint

grades_list = []

print(grades_list)
while True:
    command = int(input('Введите команду: (1 - пересдача экзамена, 2 - выходит ли стипендия, '
                        '3 - отсортированный список оценок, 4 - выход): '))

    for i in range(10):
        input_grade = int(input(f"Введите оценки студента: "))
        while input_grade not in range(1, 13):
            print("Введите значение от 1 до 12")
            grade = int(input(f"Введите верное значение: "))
        grades_list.append(input_grade)
    print("Список оценок:", grades_list)

    if command == 1:
        grades_list[int(input('Введите индекс оценки: '))] = int(input('Введите замену: '))
        print(grades_list)

    elif command == 2:
        avg_grade = sum(grades_list) / len(grades_list)
        if avg_grade>= 10.7:
            print('Стипендия присутствует')
        else:
            print('Стипендия отсутствует')

    elif command == 3:
        sort_ascending = sorted(grades_list)
        sort_descending = sorted(grades_list, reverse=True)
        print(f'Сортировка по возрастанию: {sort_ascending}; \nпо убыванию: {sort_descending}')

    elif command == 4:
        break

print('Программа завершена')

