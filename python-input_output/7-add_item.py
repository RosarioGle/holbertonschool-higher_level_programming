#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys
import os

FILENAME = "add_item.json"

def main():
    """
    main function to handle arguement addition and JSON file update
    """
    if os.path.exists(FILENAME):
        items = load_from_json_file(FILENAME)
    else:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, FILENAME)

if __name__ == "__main__":
    main()
