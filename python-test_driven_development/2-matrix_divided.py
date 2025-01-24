#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
    This function divides all elements of a matrix

    Args:
        - matrix (list of lists): two dimension matrix
        - div (int, float): divisor

    Return:
        The list of lists: all elements divided inside a new matrix

    Raises:
        TypeError: if the matrix is not a lits of interger or float
        of intergers or floats,
            or if each row of the matrix does not have hte same size,
            of if the divisor is not a number.
        ZeroDivisionError: if the divisor is zero.
    """

    error = "matrix must be a matrix (list of lists) of intergers/floats"
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error)
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(error)
        len_row = len(matrix[0])
        if not all(len(row) == len_row for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("divmust by zero")
        new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
        return new_matrix
