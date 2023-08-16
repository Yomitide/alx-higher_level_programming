#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    return dict(map(lambda a: (a[0], a[1] * 2), a_dictionary.items()))
