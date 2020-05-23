#!/usr/bin/python3
"""
This module containts one function: matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix divided by div
    """

    if len(matrix) is 0 or type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for element in matrix:
        if type(element) is not list or len(element) is 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(element) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if not all(type(n) is int or type(n) is float for n in element):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    new_matrix = []
    for element in matrix:
        new_element = [round(n / div, 2) for n in element]
        new_matrix.append(new_element)
    return new_matrix

