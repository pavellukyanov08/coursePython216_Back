# Task 1
# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     # 1
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node
#         new_node.prev = current_node
#
#     # 2
#     def remove(self, value):
#         if self.head is None:
#             print('Список пуст!')
#         else:
#             current_node = self.head
#             while current_node:
#                 if current_node.value == value:
#                     if current_node.prev is None:
#                         self.head = current_node.next
#                         current_node.next.prev = None
#                     elif current_node.next is None:
#                         current_node.prev.next = None
#                     else:
#                         current_node.prev.next = current_node.next
#                         current_node.prev.next = current_node.prev
#                     current_node = current_node.next
#                 else:
#                     current_node = current_node.next
#
#     # 3
#     def show(self, reverse=False):
#         if self.head is None:
#             print('Список пустой')
#             return
#
#         current_node = self.head
#
#         if reverse:
#             while current_node.next is not None:
#                 current_node = current_node.next
#
#         while current_node is not None:
#             print(current_node.value)
#             if reverse:
#                 current_node = current_node.prev
#             else:
#                 current_node = current_node.next
#
#     # 4
#     def is_contains(self, value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     # 5
#     def replace(self, old_value, new_value, all_occurrences=False):
#         current_node = self.head
#         while current_node:
#             if current_node.value == old_value:
#                 current_node.value = new_value
#             if not all_occurrences:
#                 return
#             current_node = current_node.next
#         return
#
#
# linked_list = LinkedList()
#
# while True:
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения введенного числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     print("6. Выйти")
#     choice = int(input("Выберите действие: "))
#
#     if choice == 1:
#         number = int(input("Введите число: "))
#         # if linked_list.is_contains(number):
#         #     print("Число уже есть в списке")
#         # else:
#         linked_list.append(number)
#         print("Число добавлено в список")
#
#     elif choice == 2:
#         number = int(input("Введите число: "))
#         linked_list.remove(number)
#
#     elif choice == 3:
#         reverse = input('Хотите перевернуть список (y/n)?: ')
#         if reverse.lower() == 'y':
#             linked_list.show(reverse=True)
#         else:
#             linked_list.show()
#
#     elif choice == 4:
#         number = int(input("Введите число: "))
#         if linked_list.is_contains(number):
#             print("Число есть в списке")
#         else:
#             print("Числа нет в списке")
#
#     elif choice == 5:
#         number = int(input("Введите число, которое нужно заменить: "))
#         new_num = int(input("Введите новое число: "))
#         if linked_list.is_contains(number):
#             only_first = input('Хотите заменить только первое вхождение (y/n)?: ')
#             if only_first.lower() == 'y':
#                 linked_list.replace(number, new_num)
#                 print(f'Первое найденное число {new_num} было заменено на {new_num}')
#             else:
#                 linked_list.replace(number, new_num, all_occurrences=True)
#                 print(f'Все числа {number} были заменены на {new_num}')
#         else:
#             print(f'Число {number} отсутствует в списке')
#     elif choice == 6:
#         break
#
# print('Программа завершена')


# Task 2
class StringStack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    # 1
    def push(self, value: str):
        if len(self.stack) < self.size:
            self.stack.append(value)
            print(f'Строка "{value}" была добавлена в стек')
        else:
            print("Стек заполнен, добавление строки невозможно")

    # 2
    def pop(self):
        if len(self.stack) > 0:
            print(f'Строка "{self.stack.pop()}" была удалена из стека')
        else:
            print('Стек пустой, удаление невозможно')

    # 3
    def count(self):
        print(f'Количество строк в стеке равно: {len(self.stack)}')

    # 4
    def is_empty(self):
        if len(self.stack) == 0:
            print('Стек пустой')

    # 5
    def is_full(self):
        if len(self.stack) == self.size:
            print('Стек заполнен')

    # 6
    def peek(self):
        if len(self.stack) > 0:
            string = self.stack[-1]
            print(f"Верхняя строка в стеке - это: {string}")
        else:
            print("Стек пустой!")

    # 7
    def clear(self):
        self.stack.clear()
        print('Стек очищен')

    def __str__(self):
        return ' -> '.join(self.stack)


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
        stack.push(stack_str)
        print(stack)

    elif choice == "2":
        stack.pop()

    elif choice == "3":
        stack.count()

    elif choice == "4":
        stack.is_empty()

    elif choice == "5":
        stack.is_full()

    elif choice == "6":
        stack.clear()

    elif choice == "7":
        stack.peek()

    elif choice == "0":
        print("Завершение программы...")
        break

    else:
        print("Неверная команда")


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
