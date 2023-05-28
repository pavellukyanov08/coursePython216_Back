# Task 1


# class NumberList:
#     @staticmethod
#     def summ_lst(lst):
#         return sum(lst)
#
#     @staticmethod
#     def avg_lst(lst):
#         return round(sum(lst) / len(lst), 2)
#
#     @staticmethod
#     def max_elem_lst(lst):
#         return max(lst)
#
#     @staticmethod
#     def min_elem_lst(lst):
#         return min(lst)
#
#     @staticmethod
#     def print_result(lst):
#         return lst
#
#
# numlist = NumberList()
#
# print(f'Вывод всего списка: {numlist.print_result([10, 2, 4, 15, 6, 2, 20])}')
#
# print(numlist.summ_lst([10, 2, 4, 15, 6, 9, 20]))
# print(numlist.avg_lst([10, 2, 4, 15, 6, 9, 20]))
# print(numlist.max_elem_lst([10, 2, 4, 15, 6, 9, 20]))
# print(numlist.min_elem_lst([10, 2, 4, 15, 6, 9, 20]))


# Task 2
class DifferentOperation:

    def __init__(self):
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def convert_to_octal_system(self):
        return oct(self.value)[2:]

    def convert_to_hex_number(self):
        return hex(self.value)[2:]

    def convert_to_bin_number(self):
        return bin(self.value)[2:]


# operation = DifferentOperation()
#
# print(operation.convert_to_octal_system())
# print(operation.convert_to_hex_number())
# print(operation.convert_to_bin_number())
