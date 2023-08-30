#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 3-square.py)
"""
class Square:
    """
    Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value):
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self):
    """

    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
