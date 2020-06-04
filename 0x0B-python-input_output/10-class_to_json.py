#!/usr/bin/python3
"""class_to_json() module"""


def class_to_json(obj):
    """Return  dictionary description for JSON serialization"""
    return obj.__dict__
