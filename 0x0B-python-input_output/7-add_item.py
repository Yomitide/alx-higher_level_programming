#!/usr/bin/python3
""" A function that adds all arguments to a Python
    list, and then save them to a file:
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    if (os.path.exists(filename)):
        existing_content = load_from_json(filename)
    else:
       existing_content = []
    existing_content.extend(args)
    save_to_json(existing_content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
