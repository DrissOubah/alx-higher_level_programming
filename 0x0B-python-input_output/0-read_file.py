#!/usr/bin/python3
"""
function that reads a text file UTF8
and prints it to stdout
"""


def read_file(filename=""):
        #reads a text file UTF8
        with open(filename, encoding="utf-8") as f:
                read_data = f.read()
        #prints it to stdout
        print(read_data,end="")
