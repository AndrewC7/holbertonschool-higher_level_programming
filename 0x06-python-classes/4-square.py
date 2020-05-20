#!/usr/bin/python3
"""Defines Square with area"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initiize Data"""
        self.__size = size

    @property
    def size(self):
        """Get Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set Size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Square Area"""
        return self.__size ** 2
