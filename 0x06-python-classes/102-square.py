#!/usr/bin/python3
"""The Beginning of a square's creation
"""


class Square:
def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Determines the area of our square
        Returns:
            the area of the square, an error otherwise
        """
        floater = isinstance(self.__size, float)
        if not isinstance(self.__size, int) or not floater:
            raise TypeError('size must be an number')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size ** 2

    @property
    def size(self):
        """The size given as our square size"""
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError('size must be an number')
            elif value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        except ValueError as e:
            print(f"{e}")

    def __le__(self, rival):
        if isinstance(rival, Square):
            return self.__size <= rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")

    def __lt__(self, rival):
        if isinstance(rival, Square):
            return self.__size < rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")

    def __gt__(self, rival):
        if isinstance(rival, Square):
            return self.__size > rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")

    def __ge__(self, rival):
        if isinstance(rival, Square):
            return self.__size >= rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")

    def __eq__(self, rival):
        if isinstance(rival, Square):
            return self.__size == rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")

    def __ne__(self, rival):
        if isinstance(rival, Square):
            return self.__size != rival.__size
        else:
            raise TypeError("Cannot compare non-Square obj")
