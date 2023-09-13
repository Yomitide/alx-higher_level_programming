#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8) and returns the number of characters added
"""

def append_write(filename="", text=""):
    """A function that appends a string to the end of a text file and returns number of characters added"""
    with open(filename, mode="a", encoding="UTF-8") as f:
        num = f.write(text)

    return num
