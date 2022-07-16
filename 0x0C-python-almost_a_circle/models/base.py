#!/usr/bin/python3
"""
Module: base.py
"""

import json
import os.path


class Base:
    """
    a class 'Base' with
    a class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiates a new instance
        """

        if id:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation
        of a dict
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)

        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json representation to a file
        """
        if list_objs:
            dic = [obj.to_dictionary() for obj in list_objs]

        with open("{}.json".format(cls.__name__), 'w+') as f:
            if list_objs:
                f.write(cls.to_json_string(dic))

            else:
                f.write('[]')

    @staticmethod
    def from_json_string(json_string):
        """decodes json string from file
        """

        if json_string:
            return json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of 'cls'
        """
        if cls.__name__ == "Rectangle":
            res = cls(5, 8)
        if cls.__name__ == "Square":
            res = cls(5)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """loads object from a json file
        """

        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                result = cls.from_json_string(f.read())
            lst = [cls.create(**i) for i in result]
            return lst
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a csv file
        """
        filename = "{}.csv".format(cls.__name__)
        with open(fname, "w") as f:
            writer = csv.write(f)
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ = "Rectangle":
                        writer.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
                    if cls.__name__ = "Square":
                        writer.writerow([obj.id, obj.width, obj.x, obj.y])
            else:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a csv file
        """
        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                rows = csv.DictReader(file)
                for row in rows:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws a shape of rect & square
        """
        for i in list_rectangles + list_squares:

            tur = turtle.Turtle()
            tur.shape("turtle")
            turtle.bgcolor("black")
            tur.fillcolor("white")
            tur.begin_fill()
            tur.pen(fillcolor="white", pencolor="red", pensize=2)
            for i in range(2):
                tur.forward(i.width)
                tur.right(90)
                tur.forward(i.height)
                tur.right(90)

            tur.end_fill()
            turtle.done()
