#!/usr/bin/python3
"""My say_my_name module
Takes in the first and last name
No importing done, no unique functions
Prints the name of a person
"""


def say_my_name(first_name, last_name=""):
    """Prints: My name is 'first_name last_name'
    The first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if first_name is None and last_name is None:
        raise TypeError('first_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
