#!/usr/bin/python3
"""A class list that inherits from list"""


class MyList(list):
    """ inherit from the classs list"""

    def __init__(self):
        """initialises the object"""

        super().__init__()

    def print_sorted(self):
        """prints the sorted list in ascending order"""

        print(sorted(self))
