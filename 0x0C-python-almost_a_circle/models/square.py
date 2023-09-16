#!/usr/bin/python3
"""class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """square class implentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """init initialization
        args:
        size: size of square
        x: x position
        y: y position
        id: object id
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """overloading string method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
    @property
    def size(self):
        """getter for size"""
        return self.width
    
    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assign the class with attributes"""
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

            def to_dictionary(self):
                """return dictionary representation"""
                return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
