#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Function for sorting"""

    def print_sorted(self):
        print(sorted(self))
