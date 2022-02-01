#!/usr/bin/python3
import json
"""function that returns an object
(Python data structure) represented
by a JSON string"""


def from_json_string(my_str):
    """Define from_json_string function"""
    return json.loads(my_str)
