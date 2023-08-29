#!/usr/bin/python3
"""
A class square that defines a square based on the previous suares
"""

class Square:
    """
    class square with attribute of size with instantiation
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

