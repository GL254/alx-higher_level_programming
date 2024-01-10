#!/usr/bin/python3

import json


def from_json_string(my_str):
    """from_json_string function
    Converts from json string back to data structure
    """
    returned = json.loads(my_str)
    return returned
