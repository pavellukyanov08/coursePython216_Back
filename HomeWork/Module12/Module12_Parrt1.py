# employees_file = 'employees.txt'
#
#
# def loading_employees():
#     employees_list = []
#     with open(file=employees_file, mode='r', encoding='utf-8') as emp_file:
#         for line in emp_file:
#             name, surname, age, post, salary = line.strip().split(',')
#             employees_list.append([name, surname, age, post, salary])
#     print(*employees_list)
#
#
# def saving_employees(employees_list):
#     with open(file=employees_file, mode='w', encoding='utf-8') as emp_file:
#         for employee in employees_list:
#             emp_file.write(f"{employee['last_name']},"
#                            f"{employee['first_name']},"
#                            f"{employee['age']},"
#                            f"{employee['position']}"
#                            f"{employee['salary']}")
#
#
# def add_employee(employees_list):
#     name = input('Введите имя сотрудника: ')
#     surname = input('Введите фамилию сотрудника: ')
#     age = int(input('Введите возраст сотрудника: '))
#     post = input('Введите должность сотрудника: ')
#     salary = float(input('Введите зарплату сотрудника: '))
#     print(employees_list)
#     employee = [name, surname, age, post, salary]
#     employees_list.append(employee)
#
#     print(f'Сотрудник был добавлен. \nТекущий список сотрудников: *{employees_list}')
#
#
# def edit_employee(employees_list):
#     surname = input('Введите фамилию сотрудника: ')
#     if surname in employees_list:
#         employees_list[surname] = {'name': input('Введите имя сотрудника'),
#                               'age': int(input('Введите возраст сотрудника')),
#                               'post': input('Введите зарплату сотрудник'),
#                               'salary': int(input('Enter new salary'))}
#         print(f'Данные сотрудника изменены. \n{employees_list}')
#     else:
#         print('Искомый сотрудник не найден')
#
#
# def delete_employee(employees_list):
#     surname = int(input('Введите фамилию сотрудника для удаления: '))
#     del employees_list[surname]
#     print(employees_list)
#
#
# def search_by_surname(employees_list):
#     surname = input('Введите фамилию сотрудника: ')
#     if surname in employees_list:
#         print(f"Employee found: {employees_list[surname]['name']}, "
#               f"{employees_list[surname]['age']} "
#               f"{employees_list[surname]['post']}")
#     else:
#         print('Сотрудник не найден')
#
#
# def choice_command():
#     employees_list = loading_employees()
#     while True:
#         command = int(input('Выберите команду: '
#                             '1 - вывод списка сотрудников, '
#                             '2 - добавление, '
#                             '3 - редактирование, '
#                             '4 - удаление, '
#                             '5 - поиск по фамилии, '
#                             '6 - выход (с сохранением): '))
#
#         if command == 1:
#             employees_list = loading_employees()
#
#         elif command == 2:
#             employees_list = add_employee(employees_list)
#
#         elif command == 3:
#             employees_list = edit_employee(employees_list)
#
#         elif command == 4:
#             employees_list = delete_employee(employees_list)
#
#         elif command == 5:
#             employees_list = search_by_surname(employees_list)
#
#         else:
#             saving_employees(employees_list)
#             break
#
#     print('Программа завершена')
#
#
# if __name__ == '__main__':
#     choice_command()


employees_file = 'employees.txt'


def loading_employees():
    employees_list = []
    with open(employees_file, mode='r', encoding='utf-8') as emp_file:
        for line in emp_file:
            name, surname, age, post, salary = line.strip().split(',')
            employees_list.append([name, surname, age, post, salary])
    return employees_list


def saving_employees(employees_list):
    with open(employees_file, mode='w', encoding='utf-8') as emp_file:
        for employee in employees_list:
            emp_file.write(f"{employee['name']}, "
                           f"{employee['surname']}, "
                           f"{employee['age']}, "
                           f"{employee['position']}, "
                           f"{employee['salary']}\n")


def add_employee(employees_list):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    position = input('Введите должность: ')
    salary = float(input('Введите зарплату: '))
    employee = [name, surname, age, position, salary]
    employees_list.append(employee)

    print(*employees_list)


def edit_employee(employees_list):
    eml_id = int(input('Введите номер сотрудника для редактирования: '))
    if eml_id < len(employees_list):
        name = input('Введите фамилию: ')
        surname = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        position = input('Введите должность: ')
        salary = float(input('Введите зарплату: '))
        employee = [name, surname, age, position, salary]
        employees_list[eml_id] = employee
        return employees_list
    else:
        print('Введенный номер сотрудника некорректен')


def delete_employee(employees_list):
    index = int(input('Введите номер сотрудника для удаления: '))
    if id < len(employees_list):
        del employees_list[index]
    else:
        print('Некорректный номер сотрудника')
    return employees_list


def search_by_surname(employees_list):
    surname = input('Введите фамилию сотрудника: ')
    search_res = []
    for employee in employees_list:
        if employee['surname'] == surname:
            search_res.append(employee)
    return search_res


def choice_command():
    employees_list = loading_employees()
    while True:
        command = int(input('Выберите команду: '
                            '1 - вывод списка сотрудников, '
                            '2 - добавление, '
                            '3 - редактирование, '
                            '4 - удаление, '
                            '5 - поиск по фамилии, '
                            '6 - выход (с сохранением): '))

        if command == 1:
            for employee in employees_list:
                print(f"{employee['name']}, "
                      f"{employee['surname']}, "
                      f"{employee['age']} лет, "
                      f"{employee['position']},"
                      f" {employee['salary']} руб.")

        elif command == 2:
            employees_list = add_employee(employees_list)

        elif command == 3:
            employees_list = edit_employee(employees_list)

        elif command == 4:
            employees_list = delete_employee(employees_list)

        elif command == 5:
            search_res = search_by_surname(employees_list)
            for emp in search_res:
                print(f"{emp['name']}, "
                      f"{emp['surname']}, "
                      f"{emp['age']} лет, "
                      f"{emp['position']},"
                      f" {emp['salary']} руб.")

        else:
            saving_employees(employees_list)
            break

    print('Программа завершена')


if __name__ == '__main__':
    choice_command()
