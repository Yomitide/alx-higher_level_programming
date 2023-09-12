#!/usr/bin/python3
"""
Module 101-add_attribute, a function that adds a new attribute to an object
"""


def add_attribute(obj, attribute, value):
    """
    add attribute to object if possible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
