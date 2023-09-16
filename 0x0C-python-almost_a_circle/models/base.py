#!/usr/bin/python3
"""A class called Base which is going to be the parent of the classes of this project"""

import os
import json

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
    @staticmethod
    def to_json_string(list_dictionaries):
        """adding static method to return the json string representation of list of dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classicmethod
