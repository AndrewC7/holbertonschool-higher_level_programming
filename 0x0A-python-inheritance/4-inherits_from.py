#!/usr/bin/python3
"""inherits_from() module"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from
    specified class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
