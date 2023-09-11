#!/usr/bin/python3
"""A class function that returns true if the object is an instance of it"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    Args: obj: object to check, a_class: class to check against.
    """


    return True if isinstance(obj, a_class) else False
