#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py)."""

class BaseGeometry():
    """basegeometry class with a public function tht raises an exception"""

    def area(self):
        """Public instance method function that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value of the input passed"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
