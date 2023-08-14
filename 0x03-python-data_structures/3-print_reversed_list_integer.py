#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for item in my_list[::-1]:
            print("{:d}".format(item))
            """ print all int in reverse. """
