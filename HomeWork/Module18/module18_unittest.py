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

    @staticmethod
    def save_to_file(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('12345')

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            value = f.read()
            print(value)

    @staticmethod
    def convert_to_octal_system(number):
        return oct(number)

    @staticmethod
    def convert_to_hex_number(number):
        return hex(number)

    @staticmethod
    def convert_to_bin_number(number):
        return bin(number)


operation = DifferentOperation()

operation.save_to_file('write.txt')
operation.load_from_file('write.txt')

print(operation.convert_to_octal_system(42))
print(operation.convert_to_hex_number(42))
print(operation.convert_to_bin_number(42))
