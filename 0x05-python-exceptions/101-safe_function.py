#!/usr/bin/python3

def safe_function(fct, *args):
    """writes a function that executes a function safely."""
    import sys

    try:
        output = fct(*args)
        return (output)
    print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return (None)
