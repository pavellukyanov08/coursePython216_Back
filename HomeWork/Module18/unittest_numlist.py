import unittest
# Task 1
# from module18_unittest import NumberList


# class TestNumberList(unittest.TestCase):
#     def setUp(self) -> None:
#         self.lst = [10, 2, 4, 15, 6, 2, 20]
#
#     def test_summ(self):
#         self.assertEqual(59, NumberList.summ_lst(self.lst), 'Результат сложения чисел должен быть равен 59')
#
#     def test_avg(self):
#         self.assertEqual(8.43, NumberList.avg_lst(self.lst), 'Результат среднего арифметического чисел должен быть '
#                                                              'равен 8.43')
#
#     def test_max(self):
#         self.assertEqual(20, NumberList.max_elem_lst(self.lst), 'Максимальное число в списке должно быть равно 20')
#
#     def test_min(self):
#         self.assertEqual(2, NumberList.min_elem_lst(self.lst), 'Минимальное число в списке должно быть равно 2')
#
#
# if __name__ == 'main':
#     unittest.main()


# Task 2
from module18_unittest import DifferentOperation
import os


class TestNumberList(unittest.TestCase):
    def setUp(self) -> None:
        self.value = DifferentOperation()
        self.num = 42
        self.value.set_value(self.num)

    def test_set_value(self):
        self.assertEqual(42, DifferentOperation.get_value(self.value), 'Значение должно быть равно 10')

    def test_octal(self):
        self.assertEqual('52',
                         DifferentOperation.convert_to_octal_system(self.value),
                         '42 в восьмиричной системе счиления должно быть равно равен 0o52')

    def test_hex(self):
        self.assertEqual('2a',
                         DifferentOperation.convert_to_hex_number(self.value),
                         '42 в восьмиричной системе счиления должно быть равно 0x2a')

    def test_bin(self):
        self.assertEqual('101010',
                         DifferentOperation.convert_to_bin_number(self.value),
                         '42 в восьмиричной системе счиления должно быть равно 0b101010')


if __name__ == 'main':
    unittest.main()
