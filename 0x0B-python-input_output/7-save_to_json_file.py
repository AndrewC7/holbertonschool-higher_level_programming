#!/usr/bin/python3
"""save_to_json_file() module"""
import json


def save_to_json_file(my_obj, filename):
    """write object to txt file using JSON"""
    with open(filename, "w") as data:
        json.dump(my_obj, data)
