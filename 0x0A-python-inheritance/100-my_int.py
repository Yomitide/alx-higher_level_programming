#!/usr/bin/python3
"""A class myint that inherits from int"""


class MyInt(int):
    """ my int is a rebel, has ==, and != operators inverted"""

    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both equal
        """
        return self.num == other
