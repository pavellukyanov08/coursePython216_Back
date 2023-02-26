# # Task 1
# from random import randint
#
#
# def remove_largest_element():
#     matrix = [[randint(1, 100) for _ in range(5)] for _ in range(5)]
#
#     for row in matrix:
#         for element in row:
#             print(element, end='\t')
#         print()
#
#     print("-----------------", end='\n')
#
#     max_elements = []
#     for row in matrix:
#         max_elements.append(max(row))
#     summ_max_elements = sum(max_elements)
#
#     removed_elements = []  # create an empty list to store the removed elements
#     modified_matrix = matrix.copy()  # create a copy of the matrix to modify it
#
#     while modified_matrix:  # while the matrix is not empty
#         for row in modified_matrix:  # loop through each row in the matrix
#             largest_element = max(row)  # get the largest element in the row
#             removed_elements.append(largest_element)  # add the largest element to the list of removed elements
#             row.remove(largest_element)  # remove the largest
#         modified_matrix = [row for row in modified_matrix if row]  # remove empty rows from the matrix
#     print(f'Удаленные элементы: {removed_elements}, \nМатрица после удаления элементов: {[[]]} =), \n'
#           f'Максимальные элементы: {max_elements}, \nСумма максимальных элементов: {summ_max_elements}')
#
#
# remove_largest_element()


# Task 2
# def island_perimeter():
#     perimeter = 0
#     m, n = len(grid), len(grid[0])
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == 1:
#                 perimeter += 4
#                 if i > 0 and grid[i-1][j] == 1:
#                     perimeter -= 2
#                 if j > 0 and grid[i][j-1] == 1:
#                     perimeter -= 2
#     print(perimeter)
#
#
# grid = [[0, 0, 0, 0, 0],
#         [0, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0]]
#
#
# island_perimeter()


# Task 3
# def shift_matrix(grid, k):
#     m, n = len(grid), len(grid[0])
#     k = k % (m * n)
#
#     while k > 0:
#         # Move the last element in each row to the first element of the next row
#         last_elem = grid[-1][-1]
#         for i in range(m-1, 0, -1):
#             grid[i][-1] = grid[i-1][-1]
#         grid[0][-1] = last_elem
#
#         # Move each element in the row to the right
#         for i in range(m):
#             last_elem = grid[i][-1]
#             for j in range(n-1, 0, -1):
#                 grid[i][j] = grid[i][j-1]
#             grid[i][0] = last_elem
#
#         k -= 1
#
#     return grid
#
#
# print(shift_matrix())
