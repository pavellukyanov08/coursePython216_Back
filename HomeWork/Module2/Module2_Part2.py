#Task1
# day_number = int(input('Enter day of weekend (1-7): '))
#
# if day_number == 1:
#     print('Понедельник')
# elif day_number == 2:
#     print('Вторник')
# elif day_number == 3:
#     print('Среда')
# elif day_number == 4:
#     print('Четверг')
# elif day_number == 5:
#     print('Пятница')
# elif day_number == 6:
#     print('Суббота')
# elif day_number == 7:
#     print('Воскресенье')

# Дабы оптимизировать код сделал вот таким способом). 0 - понедельник, 6 - воскресенье.
# print(__import__("calendar").day_name[int(input('Enter day of weekend (0-6): '))])




#Task2
# month = int(input('Enter month (1- 12): '))
#
# if month < 1 or month > 12:
#     print('Enter current month')
# else:
#     print(__import__("calendar").month_name[month])





#Task3
# num = int(input('Enter number: '))
#
# isPovitive = 'Number is positive' if num > 0 else 'Number is negative' if num < 0 else 'Number is equal to zero'
# print(isPovitive)




#Task4
# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))
#
# new_num = []
#
# if num1 != num2:
#     new_num.append(num1)
#     new_num.append(num2)
#     new_num.sort()
#     print(f'Отсортированные числа: {new_num}')
# else:
#     print(f'Исходные числа: {num1, num2}')



