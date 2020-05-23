#!/usr/bin/python3
"""
This module has one function: print_square()
"""


def print_square(size):
    """
    Prints square of #s
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print(('#' * size + '\n') * size, end='')
