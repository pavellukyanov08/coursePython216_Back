# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
# class New(Singleton):
#     pass
#
#
# a = New()
# b = New()
#
# print(id(a))
# print(id(b))
#
# print(a is b)


# Task 1
# class Logger:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         cls.__init__(cls._instance)
#         return cls._instance
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     with open(file='file.txt', mode='w', encoding='utf-8') as f:
#         numbers = [int(input('Число: ')) for _ in range(5)]
#         f.write(f'Все числа: {str(numbers)}\n')
#         f.write(f'Минимальное: {str(min(numbers))}\n')
#         f.write(f'Максимальное: {str(max(numbers))}')
#         print(f'Все числа: {numbers}')
#         print(f'Минимальное: {min(numbers)}')
#         print(f'Максимальное: {max(numbers)}')


class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []