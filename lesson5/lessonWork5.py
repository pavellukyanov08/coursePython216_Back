# spisok = []
# for i in range(10):
#     spisok.append(int(input('Введите число: ')))
#
# search_num = int(input('Искомое число: '))
# count = 0
# for i in range(len(spisok)):
#     if i == search_num:
#         count += 1
# print(f'Количество чисел {spisok}: {count}')


# spisok.pop(1)
# # spisok.remove(2)
# print(spisok)
# for i in  range(len(spisok)):
#     spisok[i] *= 2
# spisok.extend([1, 1])
# print(spisok)


# numbers = []
# summ = 0
# avg = 0
# for i in range(10):
#     numbers.append(int(input('Введите число: ')))
#     for i in numbers:
#         sum += i
#     print(f'Сумма чисел: {summ}')
#
# print(f'Среднее арифметическое: {summ / len(numbers)}')


# spisok = [1, 2, 3, 4, 5, 6, 7]
#
# print(spisok)
# print(spisok[::-1])
# print(spisok[0::2])
# print(spisok[1::2])
#
# print(spisok[0:1])
# print(spisok[-1:])
# print(spisok[3:4])
#
# print(spisok[4:])
# print(spisok[-3:-6:-1])
# print(spisok[2:5])


# numbers = []
# for i in range(1, 11):
#     numbers.extend([i ** 2])
# print(f': {numbers}')

# num_list = []
# lnt = int(input('Введите длину списка: '))
# for i in range(lnt):
#     num = int(input('Введите число кратное 3: '))
#     if num % 3 == 0:
#         num_list.append(num)
#     else:
#         print(f'{num} не делится на 3 без остатка')
#
# print(num_list)


# numbers = [x * 2 for x in range(10)]
# print(numbers)


# num_list1 = [1, 2, 3]
# num_list2 = [11, 22, 33]
# num_list3 = []
# for i in range(len(num_list1)):
#     num_list3.append(num_list1[i])
#     num_list3.append(num_list2[i])
# print(num_list3)