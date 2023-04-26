# Task 1
# num_list = [int(input("Введите число: ")) for i in range(5)]
# print(num_list)
#
# while True:
#     print("Меню:")
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     print("6. Выход")
#
#     command = int(input('Выберите пункт меню: '))
#
#     if command == 1:
#         num = int(input('Введите число: '))
#         if num not in num_list:
#             num_list.append(num)
#             print(f'Число {num} успешно добавлено в список. Текущий список: {num_list}')
#         else:
#             print('Число уже существует в списке!')
#
#     elif command == 2:
#         num = int(input("Введите число для удаления: "))
#         count = num_list.count(num)
#         if count == 0:
#             print("Число не найдено в списке.")
#         else:
#             numbers = [x for x in num_list if x != num]
#             print(f"Число удалено из списка {count} раз(а). Текущий список: {numbers}")
#
#     elif command == 3:
#         choice = int(input('1 - начало списка, 2 - конец'))
#         if choice == 1:
#             print(num_list)
#         else:
#             print(num_list[::-1])
#
#     elif command == 4:
#         num = int(input('Введите число: '))
#         if num in num_list:
#             print("Число найдено в списке.")
#         else:
#             print("Число не найдено в списке.")
#
#     elif command == 5:
#         num = int(input("Введите число для замены: "))
#         new_num = int(input("Введите новое число: "))
#         replace_all = input("Заменить все вхождения? (y/n): ")
#         if replace_all.lower() == "y":
#             num_list = [new_num if x == num else x for x in num_list]
#             print(f"Число {num} заменено на {new_num} в списке {num_list.count(new_num)} раз(а). Новый список: {num_list}")
#         else:
#             try:
#                 index = num_list.index(num)
#                 num_list[index] = new_num
#                 print("Число заменено в списке.")
#             except ValueError:
#                 print("Число не найдено в списке.")
#
#     elif command == 6:
#         break
#
# print('Программа завершена')


# Task 2
class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, value):
        if len(self.stack) == self.size:
            return 'Стек заполнен!'
        else:
            self.stack.append(value)

    def pop(self):
        return self.is_empty() or self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_full(self):
        if len(self.stack) == self.size:
            return 'Стек заполнен'

    def is_empty(self):
        if len(self.stack) == 0:
            return 'Стек пустой'

    def peek(self):
        return self.is_empty() or self.stack[-1]

    def clear(self):
        self.stack.clear()


stack = StringStack(3)

while True:
    print("Меню:")
    print("1. Добавление строки")
    print("2. Выталкивание строки")
    print("3. Подсчет строк в стеке")
    print("4. Проверка стека на пустоту")
    print("5. Проверка стека на переполнение")
    print("6. Очистка стека")
    print("7. Получение значения без выталкивания строки из стека")
    print("0. Выход")

    choice = input("Выберите команду: ")

    if choice == "1":
        stack_str = input("Введите строки, чтобы добавить в стек: ")
        if stack.push(stack_str):
            print("Строка добавлена в стек")
        else:
            print("Стек заполнен!")
    elif choice == "2":
        stack_str = stack.pop()
        if stack_str is not None:
            print("Вытолкнутая строка:", stack_str)
        else:
            print("Стек пуст!")
    elif choice == "3":
        count = stack.count_lines()
        if count == 1:
            print("В стеке имеется одна строка.")
        else:
            print(f"В стеке имеется {count} строк")
    elif choice == "4":
        if stack.is_empty():
            print("Стек пуст!")
        else:
            print("В стеке имеются строки")
    elif choice == "5":
        if stack.is_full():
            print("Стек заполнен!")
        else:
            print("В стеке есть место")
    elif choice == "6":
        stack.clear()
        print("Стек очищен")
    elif choice == "7":
        stack_str = stack.peek()
        if stack_str is not None:
            print(f"Верхняя строка стека: {stack_str}")
        else:
            print("Стек пустой!")
    elif choice == "0":
        print("Завершение программы...")
        break
    else:
        print("Неверная команда")

# print(stack.push("first"))
# print(stack.push("second"))
# print(stack.count_lines())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.push("third"))
# print(stack.push("fourth"))
# print(stack.push("fifth"))
# print(stack.push("sixth"))
# print(stack.pop())
# print(stack.count_lines())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.peek())
# stack.clear()
# print(stack.count_lines())

# class StringStack:
#     def __init__(self, size):
#         self.stack = [''] * size
#         self.top = -1
#
#     def push(self, string):
#         if self.top == len(self.stack) - 1:
#             return False
#         else:
#             self.top += 1
#             self.stack[self.top] = string
#             return True
#
#     def pop(self):
#         if self.top == -1:
#             return None
#         else:
#             string = self.stack[self.top]
#             self.top -= 1
#             return string
#
#     def count(self):
#         return self.top + 1
#
#     def is_empty(self):
#         return self.top == -1
#
#     def is_full(self):
#         return self.top == len(self.stack) - 1
#
#     def clear(self):
#         self.top = -1
#
#     def peek(self):
#         if self.top == -1:
#             return None
#         else:
#            return self.stack[self.top]
#
# #Menu
#
# stack = StringStack(5)
#
# while True:
#     print("Menu:")
#     print("1. Push a string")
#     print("2. Pop a string")
#     print("3. Count strings in stack")
#     print("4. Check if stack is empty")
#     print("5. Check if stack is full")
#     print("6. Clear stack")
#     print("7. Peek at top of stack")
#     print("0. Exit")
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         string = input("Enter a string to push onto the stack: ")
#         if stack.push(string):
#             print("String pushed onto stack.")
#         else:
#             print("Stack is full, string not pushed.")
#     elif choice == "2":
#         string = stack.pop()
#         if string is not None:
#             print("Popped string:", string)
#         else:
#             print("Stack is empty.")
#     elif choice == "3":
#         count = stack.count()
#         if count == 1:
#             print("There is 1 string in the stack.")
#         else:
#             print("There are", count, "strings in the stack.")
#     elif choice == "4":
#         if stack.is_empty():
#             print("Stack is empty.")
#         else:
#             print("Stack is not empty.")
#     elif choice == "5":
#         if stack.is_full():
#             print("Stack is full.")
#         else:
#             print("Stack is not full.")
#     elif choice == "6":
#         stack.clear()
#         print("Stack cleared.")
#     elif choice == "7":
#         string = stack.peek()
#         if string is not None:
#             print("Top string on stack:", string)
#         else:
#             print("Stack is empty.")
#     elif choice == "0":
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid choice, please try again.")
#
#
# # Use example
#
# print(stack.push("first"))
# print(stack.push("second"))
# print(stack.count())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.push("third"))
# print(stack.push("fourth"))
# print(stack.push("fifth"))
# print(stack.push("sixth"))
# print(stack.pop())
# print(stack.count())
# print(stack.is_empty())
# print(stack.is_full())
# print(stack.peek())
# stack.clear()
# print(stack.count())
