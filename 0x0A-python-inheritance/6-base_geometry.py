#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py)."""

class BaseGeometry():
    """basegeometry class with a public function tht raises an exception"""

    def area(self):
        """Public instance method function that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
