#!/usr/bin/python3
"""script that adds all arguments to a Python
list, and then save them to a file"""
from os.path import exists
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if exists(filename):
    list = load_from_json_file(filename)
    if len(sys.argv) > 0:
        for i in range(1, len(sys.argv)):
            list.append(sys.argv[i])
        save_to_json_file(list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
