#!/usr/bin/python3
"""read_lines() module"""


def read_lines(filename="", nb_lines=0):
    """read n lines from file"""
    with open(filename, "r") as data:
        if not nb_lines:
            print(data.read(), end="")
            return
        for line in data:
            print(line, end="")
            nb_lines = nb_lines - 1
            if not nb_lines:
                break
