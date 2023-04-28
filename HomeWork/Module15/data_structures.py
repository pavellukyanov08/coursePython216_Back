# Task 1
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def remove(self, value):
        if self.head is None:
            print('Список пуст!')
        else:
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    if current_node.prev is None:
                        self.head = current_node.next
                        current_node.next.prev = None
                    elif current_node.next is None:
                        current_node.prev.next = None
                    else:
                        current_node.prev.next = current_node.next
                        current_node.prev.next = current_node.prev
                    current_node = current_node.next
                else:
                    current_node = current_node.next

    def show(self):
        if self.head is None:
            print('Список пустой')
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def is_contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def replace(self, old_value, new_value):
        current_node = self.head
        while current_node:
            if current_node.value == old_value:
                current_node.value = new_value
                break
            current_node = current_node.next


linked_list = LinkedList()

while True:
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения введенного числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("6. Выйти")
    choice = int(input("Выберите действие: "))

    if choice == 1:
        number = int(input("Введите число: "))
        if linked_list.is_contains(number):
            print("Число уже есть в списке")
        else:
            linked_list.append(number)
            print("Число добавлено в список")

    elif choice == 2:
        number = int(input("Введите число: "))
        linked_list.remove(number)

    elif choice == 3:
        linked_list.show()

    elif choice == 4:
        number = int(input("Введите число: "))
        if linked_list.is_contains(number):
            print("Число есть в списке")
        else:
            print("Числа нет в списке")

    elif choice == 5:
        old_number = int(input("Введите число, которое нужно заменить: "))
        new_number = int(input("Введите новое число: "))
        linked_list.replace(old_number, new_number)

    elif choice == 6:
        break

print('Программа завершена')


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
# class StringStack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#
#     # 1
#     def push(self, value):
#         if len(self.stack) < self.size:
#             self.stack.append(value)
#             print(f'Строка {value} была добавлена в стек')
#         else:
#             print("Стек заполнен, добавление строки невозможно")
#
#     # 2
#     def pop(self):
#         if len(self.stack) > 0:
#             print(f'Строка "{self.stack.pop()}" была удалена из стека')
#         else:
#             print('Стек пустой, удаление невозможно')
#
#     # 3
#     def count(self):
#         print(f'Количество строк в стеке равно: {len(self.stack)}')
#
#     # 4
#     def is_empty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой')
#
#     # 5
#     def is_full(self):
#         if len(self.stack) == self.size:
#             print('Стек заполнен')
#
#     # 6
#     def peek(self):
#         if len(self.stack) > 0:
#             string = self.stack[-1]
#             print(f"Верхняя строка в стеке - это: {string}")
#         else:
#             print("Стек пустой!")
#
#     # 7
#     def clear(self):
#         self.stack.clear()
#         print('Стек очищен')
#
#
# stack = StringStack(3)
#
# while True:
#     print("Меню:")
#     print("1. Добавление строки")
#     print("2. Выталкивание строки")
#     print("3. Подсчет строк в стеке")
#     print("4. Проверка стека на пустоту")
#     print("5. Проверка стека на переполнение")
#     print("6. Очистка стека")
#     print("7. Получение значения без выталкивания строки из стека")
#     print("0. Выход")
#
#     choice = input("Выберите команду: ")
#
#     if choice == "1":
#         stack_str = input("Введите строки, чтобы добавить в стек: ")
#         stack.push(stack_str)
#
#     elif choice == "2":
#         stack.pop()
#
#     elif choice == "3":
#         stack.count()
#
#     elif choice == "4":
#         stack.is_empty()
#
#     elif choice == "5":
#         stack.is_full()
#
#     elif choice == "6":
#         stack.clear()
#
#     elif choice == "7":
#         stack.peek()
#
#     elif choice == "0":
#         print("Завершение программы...")
#         break
#
#     else:
#         print("Неверная команда")


# Task 3

# class StringStack:
#     def __init__(self):
#         self.stack = []
#
#     # 1
#     def push(self, value):
#         self.stack.append(value)
#         print(f'Строка {value} была добавлена в стек')
#
#     # 2
#     def pop(self):
#         if len(self.stack) > 0:
#             print(f'Строка "{self.stack.pop()}" была удалена из стека')
#         else:
#             print('Стек пустой, удаление невозможно')
#
#     # 3
#     def count(self):
#         print(f'Количество строк в стеке равно: {len(self.stack)}')
#
#     # 4
#     def is_empty(self):
#         if len(self.stack) == 0:
#             print('Стек пустой')
#
#     # 5
#     def peek(self):
#         if len(self.stack) > 0:
#             string = self.stack[-1]
#             print(f"Верхняя строка в стеке - это: {string}")
#         else:
#             print("Стек пустой!")
#
#     # 6
#     def clear(self):
#         self.stack.clear()
#         print('Стек очищен')
#
#
# stack = StringStack()
#
# while True:
#     print("Меню:")
#     print("1. Добавление строки")
#     print("2. Выталкивание строки")
#     print("3. Подсчет строк в стеке")
#     print("4. Проверка стека на пустоту")
#     print("5. Очистка стека")
#     print("6. Получение значения без выталкивания строки из стека")
#     print("7. Выход")
#
#     choice = input("Выберите команду: ")
#
#     if choice == "1":
#         stack_str = input("Введите строки, чтобы добавить в стек: ")
#         stack.push(stack_str)
#
#     elif choice == "2":
#         stack.pop()
#
#     elif choice == "3":
#         stack.count()
#
#     elif choice == "4":
#         stack.is_empty()
#
#     elif choice == "5":
#         stack.clear()
#
#     elif choice == "6":
#         stack.peek()
#
#     elif choice == "7":
#         print("Завершение программы...")
#         break
#
#     else:
#         print("Неверная команда")
