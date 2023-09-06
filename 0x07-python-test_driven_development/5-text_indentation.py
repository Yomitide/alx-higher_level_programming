#!/usr/bin/python3
"""
module 5-text indentation
contains functions that prints a text with two new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    prints text with two new line after the special characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        if char in ['.', '?', ':']:
            result += char + '\n\n'
        else:
            result += char
    print(result)
