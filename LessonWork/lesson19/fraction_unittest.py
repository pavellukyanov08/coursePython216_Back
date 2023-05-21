import unittest
# from lesson19_part2 import FractionWorking
from lesson19_part2 import NumberWorking


# class TestFractionWorking(unittest. TestCase):
#     def test_add(self):
#         self.assertEqual('Addition: 41/63', FractionWorking(3, 7) + FractionWorking(2, 9),
#                          'Результат сложения дробей 3/7 + 2/9 должен быть равен 41/63')
#
#     def test_sub(self):
#         self.assertEqual('Subtraction: 13/63', FractionWorking(3, 7) - FractionWorking(2, 9),
#                          'Результат вычитания дробей 3/7 - 2/9 должен быть равен 13/63')
#
#     def test_mult(self):
#         self.assertEqual('Multiplication: 2/21', FractionWorking(3, 7) * FractionWorking(2, 9),
#                          'Результат умножения дробей 3/7 - 2/9 должен быть равен 2/21')
#
#     def test_div(self):
#         self.assertEqual('Division: 27/14', FractionWorking(3, 7) / FractionWorking(2, 9),
#                          'Результат деления дробей 3/7 - 2/9 должен быть равен 27/14')
#
#
# if __name__ == 'main':
#     unittest.main()


class TestNumberWorking(unittest.TestCase):
    def setUp(self) -> None:
        self.num1 = 10
        self.num2 = 4

    def test_add(self):
        self.assertEqual(14, NumberWorking.add_num(self.num1, self.num2),
                         'Результат сложения дробей 3/7 + 2/9 должен быть равен 41/63')

    def test_sub(self):
        self.assertEqual(6, NumberWorking.sub_num(self.num1, self.num2),
                         'Результат вычитания дробей 3/7 - 2/9 должен быть равен 13/63')

    def test_mult(self):
        self.assertEqual(40, NumberWorking.mult_num(self.num1, self.num2),
                         'Результат умножения дробей 3/7 - 2/9 должен быть равен 2/21')

    def test_div(self):
        self.assertEqual(2.5, NumberWorking.div_num(self.num1, self.num2),
                         'Результат деления дробей 3/7 - 2/9 должен быть равен 27/14')

    def test_max(self):
        self.assertEqual(10, NumberWorking.max_num(self.num1, self.num2),
                         'Результат деления дробей 3/7 - 2/9 должен быть равен 27/14')

    def test_min(self):
        self.assertEqual(4, NumberWorking.min_num(self.num1, self.num2),
                         'Результат деления дробей 3/7 - 2/9 должен быть равен 27/14')


if __name__ == 'main':
    unittest.main()
    