#!/usr/bin/python3
"""read_file() module"""


def read_file(filename=""):
    """Print contents of text file"""
    with open(filename, 'r') as data:
        print(data.read(), end='')
