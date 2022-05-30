#!/usr/bin/python3
"""
The "2-matrix_divided" module

This module supplies one function, matrix_divided(). For example.,

>>> matrix = [[2, 4, 6], [8, 10, 12]]
>>> matrix_divided(matrix, 2)
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
"""


def matrix_divided(matrix, div):
    """Return a new matrix with the divided numbers
    Print some error if something is wrong
    """
    new_matrix = []
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if matrix == [] or matrix == [[]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    lon_row = len(matrix[0])
    for row in range(len(matrix)):
        if len(matrix[row]) != lon_row:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        for j in range(lon_row):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for h in range(len(matrix)):
        new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[h])))
    return (new_matrix)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
