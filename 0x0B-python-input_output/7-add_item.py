#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    args = sys.argv[1:]
    if os.path.exists("add_item.json"):
        args = load_from_json_file("add_item.json") + args
    save_to_json_file(args, "add_item.json")
