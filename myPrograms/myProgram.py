class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")

dog1 = Dog("Rex")
dog1.make_sound()  # выводит "Woof!"


class Engine:
    @staticmethod
    def start():
        print("Engine is started")

    @staticmethod
    def stop():
        print("Engine is stopped")

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

engine1 = Engine()
vehicle1 = Vehicle(engine1)
vehicle1.start_engine()
vehicle1.stop_engine()


class Student:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        for student in self.students:
            print(student.name)

uni = University()
student1 = Student("John")
student2 = Student("Mary")
uni.add_student(student1)
uni.add_student(student2)
uni.get_students()


class MyClass:
    def __init__(self, value):
        self.__value = value

    def __private_method(self):
        return self.__value


obj = MyClass(10)
# print(obj.__private_method()) # Вызовет ошибку AttributeError
# print(obj.__value) # Вызовет ошибку AttributeError

class MyClass:
    def __init__(self, value):
        self._value = value

    def _protected_method(self):
        return self._value


class MySubclass(MyClass):
    def __init__(self, value):
        super().__init__(value)

    def public_method(self):
        return self._protected_method()


obj = MySubclass(10)
print(obj.public_method())  # Выведет 10


class MyClass:
    def __init__(self, value):
        self._value = value

    def _protected_method(self):
        return self._value


class MySubclass(MyClass):
    def __init__(self, value):
        super().__init__(value)

    def public_method(self):
        return self._protected_method()


obj = MySubclass(10)
print(obj.public_method())  # Выведет 10

class MyClass:
    def __init__(self, value):
        self.value = value

    def public_method(self):
        return self.value

obj = MyClass(10)
print(obj.public_method())


class Car:
    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission


class Engine:
    def __init__(self, model):
        self.model = model


class Car:
    def __init__(self, engine_model, wheels):
        self.engine = Engine(engine_model)
        self.wheels = wheels

    def drive(self):
        print(f"Автомобиль с {self.engine.model} двигателем и {self.wheels} колесами находится в движении")

car1 = Car("V8", 4)
car1.drive()

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Woof!"

my_dog = Dog("Fido")
print(f'Вывод имени: {my_dog.name};\nВывод звука: {my_dog.make_sound()}')


# Создание класса
# class Student:
#     # конструктор класса, задаются атрибуты (поля класса)
#     def __init__(self, name, group, num_recbook):
#         self.name = name
#         self.group = group
#         self.num_recbook = num_recbook
#
#     def print_info(self): # создаются методы (функции) класса
#         print(f'Имя: {self.name};\n '
#               f'группа: {self.group};\n '
#               f'номер зачетной книжки: {self.num_recbook}')
#
#
# # Создание экземпляра класса, в который передаются значения для полей класса
# s = Student('Alex', 123, 321)
# # вызов метода класса для вывода информации на экран
# s.print_info()



# import webbrowser as wb, cowsay as cw, time
#
# user_say = input('Enter some word: ')
#
# if user_say == 'Христос Воскрес':
#     print('3...')
#     time.sleep(1)
#     print('2...')
#     time.sleep(1)
#     print('1...')
#     time.sleep(1)
#     cw.cow('Ну... Понеслась...')
#     wb.open('https://www.youtube.com/watch?v=Xv-kQqgE5HE&ab_channel=popugzaputina')

# class People:
#     def __int__(self, name, age, sex, isMarried):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.isMarried = isMarried
#
#     def first_people(self):
#         print('Имя:', self.name, '; возраст:', self.age, '; пол:', self.sex, '; статус:', self.isMarried)
#
#
# people1 = People('John', 21, 'male', True)
# people2 = People('Sarah', 25, 'female', False)
#
# people1.first_people()
# class People:
#     def __init__(self, name=None, age=None, sex=None, isMarried=None):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.isMarried = isMarried
#
#     def first_people(self):
#         print(f'Имя: {self.name}; возраст: {self.age}; пол: {self.sex}; статус: {self.isMarried}')
#
# people1 = People('John', 25, 'male', True)
# people2 = People('Sarah', 20, 'female', False)
#
# people1.first_people()
# people2.first_people()


# import re
#
# match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12')
# print(match[0] if match else 'Not found', '\n') # -> 23-12
#
#
# match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')
# print(match[0] if match else 'Not found', '\n') # -> Not found
#
#
# match = re.fullmatch(r'\d\d\D\d\d', r'12-12')
# print('YES' if match else 'NO', '\n') # -> YES
#
#
# match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12')
# print('YES' if match else 'NO', '\n') # -> NO
#
#
# print(re.split(r'\W+', 'Где, скажите мне, мои очки??!'), '\n')
# # -> ['Где', 'скажите', 'мне', 'мои', 'очки', '']
#
#
# print(re.findall(r'\d\d\.\d\d\.\d{4}',
#                  r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'), '\n')
# # -> ['19.01.2018', '01.09.2017']
#
#
# for m in re.finditer(r'\d\d\.\d\d\.\d{4}',
#                      r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
#     print('Дата', m[0], 'начинается с позиции', m.start(), '\n')
# # -> Дата 19.01.2018 начинается с позиции 20
# # -> Дата 01.09.2017 начинается с позиции 45
#
#
# print(re.sub(r'\d\d\.\d\d\.\d{4}',
#              r'DD.MM.YYYY',
#              r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'))
# # -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY
