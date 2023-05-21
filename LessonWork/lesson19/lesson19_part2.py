# assert, condition, message

# password = input('Введите пароль: ')
# assert password == '1234', 'Неверный пароль'


# def summ(*args):
#     return sum(args)
#
#
# def test_summ():
#     result = ''
#     try:
#         num = summ(1, 2, 3)
#         assert summ(1, 2, 3) != 6, 'Result of the function with arguments' \
#                                    f'1, 2, 3 should be 6, not {num}'
#         result += '1. OK'
#     except AssertionError as e:
#         result += f'1. Failed({e})\n'
#
#     try:
#         assert summ() == 0, 'Result of the function without arguments' \
#                                    'should be 0!'
#         result += '2. OK\n'
#     except AssertionError as e:
#         result += f'2. Failed({e})\n'
#
#     try:
#         assert summ(-5, 5, 0) == 0, 'Result of the function with arguments' \
#                                     '-5, 5, 0 should be 6'
#         result += '3. OK\n'
#     except AssertionError as e:
#         result += f'3. Failed({e})\n'
#
#     print(result)
#
#
# test_summ()


# import unittest
#
#
# def summa(*args):
#     return sum(args)
#
#
# class TestSumma(unittest. TestCase):
#     def test_summa(self):
#         num = summa(1, 2, 3)
#         self.assertEqual(num, 6, 'Result of the function with arguments' \
#                                 f'1, 2, 3 should be 6, not {num}')
#
#         self.assertEqual(summa(), 0, 'Result of the function without arguments' \
#                                     'should be 0!')
#
#         self.assertEqual(summa(-5, 5, 0), 0, 'Result of the function with arguments' \
#                                             '-5, 5, 0 should be 6')
#
#
# if __name__ == 'main':
#     unittest.main()


# from fractions import Fraction as Fr
#
#
# class FractionWorking:
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def denominator(self, value):
#         if value == 0:
#             raise ValueError('Знаменатель не может быть нулем!')
#         else:
#             self.denominator = value
#
#     def __add__(self, other):
#         new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return f'Addition: {FractionWorking.__simplify(new_numerator, new_denominator)}'
#
#     def __sub__(self, other):
#         new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return f'Subtraction: {FractionWorking.__simplify(new_numerator, new_denominator)}'
#
#     def __mul__(self, other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return f'Multiplication: {FractionWorking.__simplify(new_numerator, new_denominator)}'
#
#     def __truediv__(self, other):
#         new_numerator = self.numerator * other.denominator
#         new_denominator = self.denominator * other.numerator
#         return f'Division: {FractionWorking.__simplify(new_numerator, new_denominator)}'
#
#     @staticmethod
#     def __simplify(numerator, denominator):
#         return Fr(numerator, denominator)
#
#
# f1 = FractionWorking(3, 7)
# f2 = FractionWorking(2, 9)
#
# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)


class NumberWorking:
    @staticmethod
    def add_num(num1, num2):
        return num1 + num2

    @staticmethod
    def sub_num(num1, num2):
        return num1 - num2

    @staticmethod
    def mult_num(num1, num2):
        return num1 * num2

    @staticmethod
    def div_num(num1, num2):
        return num1 / num2

    @staticmethod
    def max_num(num1, num2):
        return max(num1, num2)

    @staticmethod
    def min_num(num1, num2):
        return min(num1, num2)


numb = NumberWorking()

print(numb.add_num(10, 4))
print(numb.sub_num(10, 4))
print(numb.mult_num(10, 4))
print(numb.div_num(10, 4))
print(numb.max_num(10, 4))
print(numb.min_num(10, 4))
