#!/usr/bin/python3
"""
This module defines the print_square function
"""


def print_square(size):
    """
    This function prints a square.
    :param size: Size of the square.
    :return: Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)