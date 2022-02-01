#!/usr/bin/python3
"""function that writes an Object to a
text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """define save_to_json_file function"""
    with open(filename, 'w+', encoding='UTF8') as fp:
        ln = json.dumps(my_obj)
        fp.writelines(ln)
    fp.close
