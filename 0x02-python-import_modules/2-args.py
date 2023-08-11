#!/usr/bin/python3

import sys
"""print no. and list of arg"""

if __name__ != "__main__":
    exit()

    arg = sys.argv
    size = len(arg) - 1
    if size == 0:
        print("zero arg")
    elif size == 1:
        print("One arg:")
    else:
        print("{}arg:".format(size))
        for i in range(size):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
