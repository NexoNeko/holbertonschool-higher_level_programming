#!/usr/bin/python3
""" Defines the add_item function """
import json
import sys
save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


try:
    items = load_file("add_item.json")
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_file(items, "add_item.json")
