#!/usr/bin/python3
"""A function that returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
    """pascal triangle function that returns list of list of integers
    """
    if n <= 0:
        return []

    pascal_list = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = C * (line - i) // i
        pascal_list.append(row)
    return pascal_list
