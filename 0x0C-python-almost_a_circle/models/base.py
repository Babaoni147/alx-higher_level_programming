#!/usr/bin/python3
"""Define a base model"""

from os import path
import json
import csv
import turtle


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of a list of objects to a file"""

        filename = cls.__name__ + '.json'

        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                write = csv.Dictwriter(f, file_names=field_names)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a csv file"""

        filename = cls.__name__ + '.json'

        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    file_nemes = ["id", "width", "height", "x", "y"]
                else:
                    file_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, file_names=fieldnames)

                new_list_dict = []

                converted_dict = {}

                for d in list_dicts:
                    for key, Value in d.items():
                        converterd_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict
                
                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))

                return list_of_instances
        except FileNotFoundError:
            return []

    @stateicmethod
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
