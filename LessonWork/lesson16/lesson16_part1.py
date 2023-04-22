# class Stack:
#     def __init__(self, iterable: list | tuple | set = None):
#         self.lst = list(iterable) if iterable else []
#
#     def push(self, value):
#         self.lst.append(value)
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'Stack is empty!'
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def size(self):
#         return len(self.lst)
#
#
# s = Stack()
# print(s.peek())
#
# s.push(1)
# print(s.peek())


# class Stack:
#     def __init__(self, size, iterable: list | tuple | set = None):
#         self.size = size
#         self.lst = list(iterable[:size]) if iterable else []
#
#     def push(self, value):
#         if not self.is_full():
#             self.lst.append(value)
#         else:
#             print('Stack is full')
#
#     def is_full(self):
#         return len(self.lst) == self.size
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'Stack is empty!'
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def size(self):
#         return len(self.lst)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.lst))
#
#
# s = Stack(3, [1, 2, 3, 4, 5])
# print(s.peek())
# print(s.pop())
# s.push(5)
# s.push(4)
# print(s.is_full())
# print(s)


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next is not None:
#             current_node.next = current_node.next
#
#         current_node.next = current_n


# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#     # Если список пустой, делаем новую ноду головой
#         if self.head is None:
#             self.head = new_node
#         return
#
#     # Если список не пустой, перебираем все ноды, пока не дойдём
#     # до последней
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#     # Добавляем нашу ноду в next последней, делая её новой последней
#         current_node.next = new_node
#         new_node.prev = current_node
#
#     def delete(self, value):
#     # Если список пустой, ничего не делаем, отдыхаем
#         if self.head is None:
#             return
#
# # Если то, что мы хотим удалить, это голова, то удаляем её
#         if self.head.value == value:
#             self.head = self.head.next
#         if self.head is not None:
#             self.head.prev = None
#         return
#
# # Если список не пустой, перебираем все ноды, пока не дойдём
# # до искомого value или до конца списка
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#             if current_node.next is not None:
#                 current_node.next.prev = current_node
#             return
#         current_node = current_node.next
#
#     def show(self):
#     # Если список пустой, выводим сообщение об этом
#         if self.head is None:
#             print('List is empty!')
#         return
#
# # Если список не пустой, перебираем и выводим все ноды
#         print('None', end=' <-> ')
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value, end=' <-> ')
#             current_node = current_node.next
#             print('None')
#
#
# a = DoubleLinkedList()
# a.append(5)
# a.append(2)
# a.append(4)
# a.append(1)
# a.show()


class Queue:
    def __init__(self, size):
        self.lst = []
        self.size = size

    def is_empty(self):
        return len(self.lst) == 0

    def is_full(self):
        return len(self.lst) == self.size

    def enqueue(self, value):
        if len(self.lst) >= self.size:
            raise ValueError('Queue is full!')
        self.lst.append(value)

    def dequeue(self):
        return self.lst.pop(0)

    def show(self):
        print(f' <- '.join(map(str, self.lst)))
#
#
# q = Queue(5)
#
# q.enqueue(3)
# q.enqueue(5)
# q.enqueue(1)
# q.enqueue(4)
# q.enqueue(3)
# q.enqueue(8)
#
# q.show()
#
# q.enqueue(10)
# print(q.dequeue())
# q.show()
# q.enqueue(10)
# q.show()


# class PriorityQueue(Queue):
#     def prior_insert(self, value):
#         if len(self.lst) >= self.size:
#             return 'Queue is full'
#
#         priority = value[1]
#         for i in range(len(self.lst)):
#             if priority > self.lst[i][1]:
#                 self.lst.insert(i, value)
#                 break
#         else:
#             self.lst.append(value)
#         index = len(self.lst) - 1
#         while index >= 0 and self.lst[index][1] < priority:
#             index -= 1
#         if index == -1:
#             index = 0
#         self.lst.insert(index, value)
#
#     def peek(self):
#         return self.lst[0][0]
#
#
# q = PriorityQueue(3)
# q.prior_insert(('Помыть посуду', 7))
# q.prior_insert(('Погулять с друзьями', 4))
# q.prior_insert(('Сделать задание', 10))
# q.prior_insert(('Сходить в магазин', 1))
# q.show()
# print(q.peek())
# print(q.dequeue())
# q.show()


