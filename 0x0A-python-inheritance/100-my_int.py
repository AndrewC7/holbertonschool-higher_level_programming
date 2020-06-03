#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """my int"""
    def __eq__(self, other):
        """check if equal"""
        return int(self) != int(other)

    def __ne__(self, other):
        """check if !equal"""
        return int(self) == int(other)
