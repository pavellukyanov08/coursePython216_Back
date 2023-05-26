import unittest
from module18_unittest import NumberList


class TestNumberList(unittest.TestCase):
    def setUp(self) -> None:
        self.lst = [10, 2, 4, 15, 6, 2, 20]

    def test_summ(self):
        self.assertEqual(59, NumberList.summ_lst(self.lst), 'Результат сложения чисел должен быть равен 59')

    def test_avg(self):
        self.assertEqual(8.43, NumberList.avg_lst(self.lst), 'Результат среднего арифметического чисел должен быть '
                                                             'равен 8.43')

    def test_max(self):
        self.assertEqual(20, NumberList.max_elem_lst(self.lst), 'Максимальное число в списке должно быть равно 20')

    def test_min(self):
        self.assertEqual(2, NumberList.min_elem_lst(self.lst), 'Минимальное число в списке должно быть равно 2')


if __name__ == 'main':
    unittest.main()