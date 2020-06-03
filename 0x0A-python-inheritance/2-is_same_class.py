#!/usr/bin/python3
"""is_same_class() module"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of specified class"""
    return type(obj) == a_class
