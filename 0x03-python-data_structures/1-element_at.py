#!/usr/bin/python3
# 1-element_at.py

"""retrieving elements from list"""
def elemen_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    return None
