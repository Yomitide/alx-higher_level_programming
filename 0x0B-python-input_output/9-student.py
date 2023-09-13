#!/usr/bin/python3
""" A module that defines a class student by public instances"""



class Student():
    """class created with public instances first_name,last_name,age"""

    def __init__(self, first_name, last_name, age):
        """initialising the public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
