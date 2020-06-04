#!/usr/bin/python3
"""number_of_lines() module"""


def number_of_lines(filename=""):
    """Return number of lines"""
    with open(filename, "r") as data:
        return len(data.readlines())
