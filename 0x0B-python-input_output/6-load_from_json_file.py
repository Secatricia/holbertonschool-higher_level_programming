#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """define load_to_json_file function"""
    with open(filename) as fp:
        fn = fp.read()
        return json.loads(fn)
