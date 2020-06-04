#!/usr/bin/python3
"""load_from_json_file() module"""
import json


def load_from_json_file(filename):
    """creates object from JSON file”"""
    with open(filename, "r") as data:
        return json.load(data)
