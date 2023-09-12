#!/usr/bin/python3
"""A function that checks the instance of a class and whether it inherits"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""

    return True if isinstance(obj, a_class) and type(obj) is not a_class else False
