#!/usr/bin/python3
"""
A function that adds 2 integers
"""
def add_integer(a, b=98):
	"""
The functions collects an int or float from user and returns the addition of the two numbers
	"""
	if not isinstance(a, (int, float)):
	   raise TypeError("a must be an integer")
	elif not isinstance(b, (int, float)):
	   raise TypeError("b must be an integer")
	else:
	     return int(a + b)
