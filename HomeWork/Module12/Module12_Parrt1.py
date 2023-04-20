employees_file = 'employees.txt'


# Функция для получения списка сотрудников из файла
def load_employees():
    employees = []
    with open(employees_file, mode='r') as file:
        for line in file:
            name, surname, age, post, salary = line.strip().split(',')
            employees.append({
                'name': name,
                'surname': surname,
                'age': age,
                'post': post,
                'salary': salary
            })
    return employees


def save_employees(employees):
    with open(employees_file, mode='w') as file:
        for employee in employees:
            file.write(f"{employee['name']}, "
                       f"{employee['surname']}, "
                       f"{employee['age']}, "
                       f"{employee['post']}, "
                       f"{employee['salary']}\n")


def add_employee(employees):
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    post = input('Введите должность: ')
    salary = float(input('Введите зарплату: '))
    employee = {
        'name': name,
        'surname': surname,
        'age': age,
        'post': post,
        'salary': salary
    }
    employees.append(employee)
    print(employees)


def edit_employee(employees):
    index = int(input('Введите номер сотрудника для редактирования: '))
    if index < len(employees):
        name = input('Введите фамилию: ')
        surname = input('Введите имя: ')
        age = int(input('Введите возраст: '))
        post = input('Введите должность: ')
        salary = float(input('Введите зарплату: '))
        employee = {
            'name': name,
            'surname': surname,
            'age': age,
            'post': post,
            'salary': salary
        }
        employees[index] = employee
        return employees
    else:
        print('Введенный номер сотрудника некорректен')
        return employees


def delete_employee(employees):
    index = int(input('Введите номер сотрудника для удаления: '))
    if index < len(employees):
        del employees[index]
    else:
        print('Некорректный номер сотрудника')
    return employees


def search_by_surname(employees):
    last_name = input('Введите фамилию для поиска: ')
    results = []
    for employee in employees:
        if employee['last_name'] == last_name:
            results.append(employee)
    return results


def choice():
    employees_list = load_employees()
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
                print(
                    f"{employee['name']} "
                    f"{employee['surname']}, "
                    f"{employee['age']} лет, "
                    f"{employee['post']}, "
                    f"{employee['salary']} руб.")

        elif command == 2:
            employees_list = add_employee(employees_list)

        elif command == 3:
            employees_list = edit_employee(employees_list)

        elif command == 4:
            employees_list = delete_employee(employees_list)

        elif command == 5:
            results = search_by_surname(employees_list)
            for employee in results:
                print(f"{employee['name']} {employee['surname']}, {employee['age']} лет, {employee['post']},"
                      f" {employee['salary']} руб.")
        elif command == 6:
            save_employees(employees_list)
            break
        else:
            print('Неверный номер команды')


if __name__ == '__main__':
    choice()
