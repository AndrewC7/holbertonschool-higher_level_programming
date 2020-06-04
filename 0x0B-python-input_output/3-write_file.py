#!/usr/bin/python3
"""write_file() module"""


def write_file(filename="", text=""):
    """Write string to txt file"""
    with open(filename, 'w') as data:
        return data.write(str(text))
