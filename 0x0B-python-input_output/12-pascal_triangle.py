#!/usr/bin/python3
"""Module with the function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])
    matrix = [[1]]
    if n >= 2:
        matrix.append([1, 1])
    for x in range(2, n):
        new_row = []
        new_row.append(1)
        for idx in range(1, len(matrix[x]) - 1):
            new_row.append(matrix[idx] + matrix[idx + 1])
        matrix.append(new_row)
    return (matrix)
