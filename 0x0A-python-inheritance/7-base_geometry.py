#!/usr/bin/python3
"""BaseGeometry module with area() and integer_validator() functions"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Raise  exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Check value"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
