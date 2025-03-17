#!/usr/bin/python3
"""
Module for class Square
"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for i in range(0, self.size):
            print(self.position[0] * ' ' + '#' * self.size)

    def area(self):
        return self.size * self.size
