#!/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)
"""
class Square:
    """
    Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value):
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self):
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Attributes:
        size (int): the size of a new square.
        position (int, int): the position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        @property
        def position(self):
            """
            Getter
            Return: position
            """
            return self.__position

    @Position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int ) for num in value) or
                not all (num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
