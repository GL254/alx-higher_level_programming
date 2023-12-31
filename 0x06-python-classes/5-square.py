#!/usr/bin/python3
"""The Beginning of a square's creation
"""


class Square:
    """A Square shape
    Creates a square shape with various properties"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Determines the area of our square """

        if not isinstance(type(self.__size), int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size ** 2

    @property
    def size(self):
        """given square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(type(self.__size), int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")
