#!/usr/bin/python3
"""Program to save strings from command
line arguments to a file called add_item.json.
"""

if __name__ == "__main":
    import sys
    import json
    from os.path import isfile

    s_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    l_f_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    if isfile(filename):
        file_data = l_f_json_file(filename)
    else:
        file_data = []

    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])

    s_to_json_file(file_data, filename)
