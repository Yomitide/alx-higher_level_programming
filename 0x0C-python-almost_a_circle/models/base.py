#!/usr/bin/python3
"""A class called Base which is going to be the parent of the classes of this project"""

import os
import json
import csv
import turtle

class Base():
    """The function Base with private and public attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """adding static method to return the json string representation of list of dictionary"""
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json representation of an object to a file
        Args:
        list_objs: list of instances
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as f:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = json.dumps(obj_list)
            f.write(json_str)
    @staticmethod
    def from_json_string(json_string):
        """hat returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set of a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls (1)
            dummy.update(**dictionary)
            return dummy
    @classmethod
    def load_from_file(cls):
        """adding the class method that returns a list of instances"""
        filename = cls.__name__ + "json"
        try:
            with open(filename, 'r') as f:
                obj_list = json.load(f)
            return [cls.create(**obj) for obj in obj_list]
        except:
            pass
        return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialising and deserializing in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])
    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        obj_list = []
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])}
                o = cls.create(**dic)
                obj_list.append(o)
        return obj_list
    @staticmethod
    def draw(list_rectangles, list_squares):
        """that opens a window and draws all the Rectangles and Squares
        args:
        list_rectangles, list_squares
        """
        window = turtle.screen()
        t = turtle.pen()
        figures = list_rectangles + list_squares
        screen.bgcolor("white")

        for fig in figures:
            t.penup()
            t.goto(fig.x, fig.y)
            t.pendown()
            t.forward(fig.width)
            t.left(90)
            t.forward(fig.height)
            t.left(90)

        for rect in list_rectangles:
            draw_rectangle(rect.x, rect.y, rect.width, rect.height)
        for square in list_squares:
            draw_rectangle(square.x, square.y, square.size, square.size)

        window.exitonclick
