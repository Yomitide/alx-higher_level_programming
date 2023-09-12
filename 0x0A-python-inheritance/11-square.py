#!/usr/bin/python3
"""Write a class square that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A square child class based on Rectangle  as it parent class"""

    def __init__(self, size):
        """private initialisation of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
