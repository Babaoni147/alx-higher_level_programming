#!/usr/bin/python3
"""Defines a base module"""
import json
from os import path
import turtle


class Base:
    """Base class

    Attribute:
        __nb_objects (int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialize base class

        Args:
            id (int): id of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a filei"""

        new_list = []
        new_file = cls.__name__ + ".json"
        if list_objs is not None:
            for el in list_objs:
                new_list.append(el.to_dictionary())
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""

        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        dummy_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        my_file = cls.__name__ + ".json"
        new_list = []
        if path.exists(my_file):
            with open(my_file, "r", encoding="utf-8") as f:
                new_dict = cls.from_json_string(f.read())
                for inst in new_dict:
                    new_list.append(cls.create(**inst))
                return new_list
        else:
            return []

    # CSV

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save string representation to CSV file"""

        new_list_csv = []
        new_csv_file = cls.__name__ + ".csv"
        if new_list_csv is not None:
            for el in list_objs:
                new_list_csv.append(el.to_dictionary())
        with open(new_csv_file, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(new_list_csv))

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instance"""

        csv_file = cls.__name__ + ".csv"
        if path.exists(csv_file):
            with open(csv_file, "r", encoding="utf-8") as file:
                csv_dict = cls.from_json_string(file.read())
                csv_list = [cls.create(**csv_inst) for csv_inst in csv_dict]
                return csv_list
        else:
            return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open window draw Rectangle and Squarse"""

        turt = turtle.Turtle()

        turt.screen.bgcolor("#FFFF00")

        turt.pensize(5)

        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtile()

            turt.up()

            turt.gotoo(rect.x, rect.y)

            turt.down()

            for _ in range(2):
                turt.forward(rect.width)

                turt.left(90)

                turt.forward(rect.height)

                turt.left(90)

            turt.hideturtle()

            turt.color("#3399FF")

        for sq in list_squares:
            turt.showturtle()

            turt.up()

            turt.goto(sq.x, sq.y)

            turt.down()

            for _ in range(2):
                turt.forward(sq.width)

                turt.left(90)

                turt.forward(sq.height)

                turt.left(90)

            turt.hidetutle()
        turtle.exitonclick()
