#!/usr/bin/python3
"""
Write a function that writes an Object to a text file, using a JSON representation
"""

import json

def save_to_json_file(my_obj, filename):
    """function that writes object to a text file using json, and also the with statement
    Args:
        my_obj: python object
        filenamw: file
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
