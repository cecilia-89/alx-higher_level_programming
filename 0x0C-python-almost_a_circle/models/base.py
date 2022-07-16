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

        if json_string:
            return json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            res = cls(5, 8)
        if cls.__name__ == "Square":
            res = cls(5)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                result = cls.from_json_string(f.read())
            lst = [cls.create(**i) for i in result]
            return lst
        return []
