#!/usr/bin/python3
"""
Module for class Square
"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        self.size = size

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

    def my_print(self):
        if self.size <= 0:
            print()
            return

        for i in range(0, self.size):
            print('#' * self.size)

    def area(self):
        return self.size * self.size
