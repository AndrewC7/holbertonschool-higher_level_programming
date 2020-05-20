#!/usr/bin/python3
"""Prints square"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initilize Data"""
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

    def my_print(self):
        """Print Square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
                print("#" * self.__size)
