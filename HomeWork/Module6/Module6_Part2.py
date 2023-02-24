# Task 1
from random import randint


def remove_largest_element():
    matrix = [[randint(1, 100) for _ in range(5)] for _ in range(5)]

    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

    print("-----------------", end='\n')

    max_elements = []
    for row in matrix:
        max_elements.append(max(row))
    summ_max_elements = sum(max_elements)

    removed_elements = []  # create an empty list to store the removed elements
    modified_matrix = matrix.copy()  # create a copy of the matrix to modify it

    while modified_matrix:  # while the matrix is not empty
        for row in modified_matrix:  # loop through each row in the matrix
            largest_element = max(row)  # get the largest element in the row
            removed_elements.append(largest_element)  # add the largest element to the list of removed elements
            row.remove(largest_element)  # remove the largest
        modified_matrix = [row for row in modified_matrix if row]  # remove empty rows from the matrix
    print(f'Удаленные элементы: {removed_elements}, \nМатрица после удаления элементов xD: {[[]]}, \n'
          f'Максимальные элементы: {max_elements}, \nСумма максимальных элементов: {summ_max_elements}')


remove_largest_element()
