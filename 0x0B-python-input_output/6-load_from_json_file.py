#!/usr/bin/python3
"""
Module 6-load_from_json_file

Write a function that creates an Object from a “JSON file”:
"""

import json

def load_from_json_file(filename):
    """function that writes object to a text file using json, and also the with statement
    Args:
        filename: file
    """
    with open(filename, mode='r', encoding="UTF-8") as f:
        return json.load(f)
