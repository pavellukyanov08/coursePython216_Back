employees = {}


employees_file = 'employees.txt'


def add_employee():
    name = input('Enter the name of employee: ')
    surname = input('Enter the surname of employee: ')
    age = int(input('Enter the age of employee: '))
    post = input('Enter the post of employee: ')
    employees[surname] = {'name': name, 'age': age, 'post': post}
    print(f'An employee has been added. \nCurrent list of employee: {employees}')
# while True:
#     command = int(input('Select command (1 - add, 2 - edit, 3 - search 4 - remove, 5 - output): '))
#
#     if command == 1:
#         def add_employee():
#             name = input('Enter the name of employee: ')
#             surname = input('Enter the surname of employee: ')
#             age = int(input('Enter the age of employee: '))
#             post = input('Enter the post of employee: ')
#
#             employees[surname] = {'name': name, 'age': age, 'post': post}
#             print(f'An employee has been added. \nCurrent list of employee: {employees}')
#
#     elif command == 2:
#         def edit_employee():
#             surname = input('Enter the surname of employee: ')
#             if surname in employees:
#                 employees[surname] = {'name': input('Enter new name'),
#                                       'age': int(input('Enter new age')),
#                                       'post': input('Enter new post')}
#                 print(f'Employee details have been changed. \n{employees}')
#             else:
#                 print('Entered employee does not exist')
#
#     elif command == 3:
#         def search_by_surname():
#             surname = input('Enter the surname of employee: ')
#
#             if surname in employees:
#                 print(f"Employee found: "
#                       f"{employees[surname]['name']}, "
#                       f"{employees[surname]['age']} "
#                       f"{employees[surname]['post']}")
#             else:
#                 print('Employee not found')

