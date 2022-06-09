#!/usr/bin/python3
"""Module with the function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])
    matrix = []
    matrix.append([1])
    if n >= 2:
        matrix.append([1, 1])
    for x in range(1, n - 1):
        new_row = []
        new_row.append(1)
        for idx in range(0, len(matrix[x]) - 1):
            new_row.append(matrix[x][idx] + matrix[x][idx + 1])
        new_row.append(1)
        matrix.append(new_row)
    return (matrix)
