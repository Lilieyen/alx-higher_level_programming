#!/usr/bin/python3
"""writing an object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
"""using with statement to write an object to a text file"""
	with open(filename, mode="w") as myfile:
		myfile.write(my_obj)
