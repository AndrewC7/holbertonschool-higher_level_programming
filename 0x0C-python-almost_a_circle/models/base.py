#!/usr/bin/python3


"""
Base Module
"""


import json
import os
from os import path


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init Data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string to file"""
        file_name = cls.__name__ + '.json'
        my_dictionay = []
        if list_objs is not None:
           my_dictionary = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, 'w') as f:
            f.write(cls.to_json_string(my_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON representations"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance w/ attributes set"""
        if cls.__name__ == 'Square':
            instsnce = cls(1)
            instance.update(**dictionary)
            return instance

        if cls.__name__ == 'Rectangle':
            instance = cls(1, 2)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Return list of instances"""
        file_name = cls.__name__ + '.json'
        if path.isfile(file_name):
            with open(file_name, 'r') as f:
                instance_list = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in instance_list]
        return []
