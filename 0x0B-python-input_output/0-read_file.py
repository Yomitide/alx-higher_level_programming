#!/usr/bin/python3
"""A function that reads a test file utf8 and prints to stdout"""



def read_file(filename=""):
    """The function using with statement to read a file"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read(), end="")
