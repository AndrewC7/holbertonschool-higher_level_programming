#!/usr/bin/python3
"""defines Square"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initialize data"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
