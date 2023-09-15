#!/usr/bin/python3
"""A class called Base which is going to be the parent of the classes of this project"""

class Base():
    """The function Base with private and public attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
