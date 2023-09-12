#!/usr/bin/python3
"""Write a class (based on 9-rectangle.py)."""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square child class based on rectangle as it parent class"""

    def __init__(self, size):
        """private initialisation of width and height set to positive standard"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
