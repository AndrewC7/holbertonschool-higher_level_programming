#!/usr/bin/python3
"""print_sorted() module"""


class MyList(list):
    """MyList"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
