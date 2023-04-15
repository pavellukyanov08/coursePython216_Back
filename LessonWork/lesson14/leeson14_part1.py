# Task 1
# class People:
#     def __init__(self, name, surname, birthday, number, country, city, address):
#         self.name = name
#         self.surname = surname
#         self.birthday = birthday
#         self.number = number
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def input_data(self):
#         self.name = input('Введите имя: ')
#         self.surname = input('Введите фамилию: ')
#         self.birthday = input('Введите дату рождения (дд.мм.гг): ')
#         self.number = int(input('Введите номер телефона: '))
#         self.country = input('Введите страну: ')
#         self.city = input('Введите город: ')
#         self.address = input('Введите адрес: ')
#
#     def output_data(self):
#         print(self.name, self.surname, self.birthday, self.number, self.country, self.city, self.address)
#
#
# people1 = People('', '', '', '', '', '', '')
#
# people1.input_data()
# people1.output_data()


# Task 2
# class Number:
#     def __int__(self, num):
#         self.num = num
#
#     def square(self):
#         return int(self.num) ** 2
#
#
# class Float(Number):
#     def square(self):
#         return self.num ** 2
#
#
# a = Number(5)
# print(a.square())
# b = Float(6)
# print(b.square())


# class Bottle:
#     def __init__(self, content):
#         self.content = content
#
#     def empty(self):
#         self.content = None
#
#
# a = Bottle('Вода')
# print(a.content)
# print(Bottle.content)
# print(a.valid)
# Bottle.empty(a)
# print(a.content)


class Triangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


S = Triangle(6, 10)

print(S.square())
print(S.perimeter())

