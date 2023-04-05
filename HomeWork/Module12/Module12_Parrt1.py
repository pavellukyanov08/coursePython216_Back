employees_file = 'employees.txt'

employees_list = []


def loading_employees():
    with open(file=employees_file, mode='r', encoding='utf-8') as emp_file:
        for line in emp_file:
            name, surname, age, post, salary = line.strip().split(',')
            employees = [name, surname, age, post, salary]
    print(employees)


def saving_employees():
    with open(file='employees_file', mode='w', encoding='utf-8') as emp_file:
        for employee in employees_list:
            emp_file.write(f"{employee['last_name']},"
                           f"{employee['first_name']},"
                           f"{employee['age']},"
                           f"{employee['position']}"
                           f"{employee['salary']}")


def add_employee():
    name = input('Введите имя сотрудника: ')
    surname = input('Введите фамилию сотрудника: ')
    age = int(input('Введите возраст сотрудника: '))
    post = input('Введите должность сотрудника: ')
    salary = float(input('Введите зарплату сотрудника: '))
    employees_list[surname] = {'name': name, 'age': age, 'post': post, 'salary': salary}
    print(f'Сотрудник был добавлен. \nТекущий список сотрудников: {employees_list}')


def edit_employee():
    surname = input('Введите фамилию сотрудника: ')
    if surname in employees_list:
        employees_list[surname] = {'name': input('Введите имя сотрудника'),
                              'age': int(input('Введите возраст сотрудника')),
                              'post': input('Введите зарплату сотрудник'),
                              'salary': int(input('Enter new salary'))}
        print(f'Данные сотрудника изменены. \n{employees_list}')
    else:
        print('Искомый сотрудник не найден')


def delete_employee():
    surname = int(input('Введите фамилию сотрудника для удаления: '))
    del employees_list[surname]
    print(employees_list)


def search_by_surname():
    surname = input('Введите фамилию сотрудника: ')
    if surname in employees_list:
        print(f"Employee found: {employees_list[surname]['name']}, "
              f"{employees_list[surname]['age']} "
              f"{employees_list[surname]['post']}")
    else:
        print('Сотрудник не найден')


def choice_command():

    while True:
        command = int(input('Выберите команду: '
                            '1 - вывод списка сотрудников, '
                            '2 - добавление, '
                            '3 - редактирование, '
                            '4 - удаление, '
                            '5 - поиск по фамилии, '
                            '6 - выход (с сохранением): '))

        if command == 1:
            loading_employees()

        elif command == 2:
            add_employee()

        elif command == 3:
            edit_employee()

        elif command == 4:
            delete_employee()

        elif command == 5:
            search_by_surname()

        else:
            saving_employees()
            break

    print('Программа завершена')


if __name__ == '__main__':
    choice_command()
