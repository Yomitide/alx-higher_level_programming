#!/usr/bin/python3
"""Write a class (based on 7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A rectangle child class based on basegeometry as it parent class"""

    def __init__(self, width, height):
        """private initialisation of width and height set to positive standard"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
