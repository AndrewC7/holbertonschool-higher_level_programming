#!/usr/bin/python3
"""append_write() module"""


def append_write(filename="", text=""):
    """Append string at end of txt file"""
    with open(filename, 'a') as data:
        return data.write(str(text))
