#!/usr/bin/python3
"""
Script that adds arguments from the command line to a Python list, and
then save them to a JSON file named: add_item.json If the file doesn’t
exist, it should be created
Most include python object to JSON string function:
Most include JSON file to python object function:
"""

import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Create a python list and check for command line arguments. When available
# save them to the newly created list
new_list = []
for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

# Open JSON file: add_item.json and create a python list using the
# load_from_json_file(filename) function
old_list = []
if os.path.exists("add_item.json"):
    old_list = load_from_json_file("add_item.json")

# Append new_list data to old_list
old_list = old_list + new_list

# Convert new_list into a json string and overwrite the json file
# dd_item.json using: save_to_json_file(my_obj, filename) function
save_to_json_file(old_list, "add_item.json")
