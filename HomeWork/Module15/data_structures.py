num_list = [int(input("Введите число: ")) for i in range(5)]
print(num_list)

while True:
    print("Меню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("6. Выход")

    command = int(input('Выберите пункт меню: '))

    if command == 1:
        num = int(input('Введите число: '))
        if num not in num_list:
            num_list.append(num)
            print(f'Число {num} успешно добавлено в список. Текущий список: {num_list}')
        else:
            print('Число уже существует в списке!')

    elif command == 2:
        num = int(input("Введите число для удаления: "))
        count = num_list.count(num)
        if count == 0:
            print("Число не найдено в списке.")
        else:
            numbers = [x for x in num_list if x != num]
            print(f"Число удалено из списка {count} раз(а). Текущий список: {numbers}")

    elif command == 3:
        choice = int(input('1 - начало списка, 2 - конец'))
        if choice == 1:
            print(num_list)
        else:
            print(num_list[::-1])

    elif command == 4:
        num = int(input('Введите число: '))
        if num in num_list:
            print("Число найдено в списке.")
        else:
            print("Число не найдено в списке.")

    elif command == 5:
        num = int(input("Введите число для замены: "))
        new_num = int(input("Введите новое число: "))
        replace_all = input("Заменить все вхождения? (y/n): ")
        if replace_all.lower() == "y":
            num_list = [new_num if x == num else x for x in num_list]
            print(f"Число {num} заменено на {new_num} в списке {num_list.count(new_num)} раз(а). Новый список: {num_list}")
        else:
            try:
                index = num_list.index(num)
                num_list[index] = new_num
                print("Число заменено в списке.")
            except ValueError:
                print("Число не найдено в списке.")

    elif command == 6:
        break

print('Программа завершена')
