#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """function returns true if the object is an instance
    Args: obj: object of the class.
    a_class:class function
    """

    return True if type(obj) ==  a_class else False
