#!/usr/bin/python3

"""A function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""

    # Check if the input matrix is valid
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if each row has the same length
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
