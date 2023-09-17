#!/usr/bin/python3
"""A class rectangle module"""
from models.base import Base

class Rectangle(Base):
    """A class rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """updating the str class rectangle instance representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of class rectangle"""
        value = self.__height * self.__width
        return value
    def display(self):
        """display function with characters in #"""
        for i in range(self.y):
            print ()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assign arguments to each attribute"""
        n_args = len(args)
        if n_args >= 1:
            self.id = args[0]
        if n_args >= 2:
            self.width = args[1]
        if n_args >= 3:
            self.height = args[2]
        if n_args >= 4:
            self.x = args[3]
        if n_args >= 5:
            self.y = args[4]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return{'x': self.x, 'y': self.y, 'id': self.id, 'width': self.width, 'height': self.height}
