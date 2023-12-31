#!/usr/bin/python3
"""The Beginning of a square's creation"""


class Square:

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
