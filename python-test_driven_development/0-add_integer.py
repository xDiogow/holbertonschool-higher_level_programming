#!/usr/bin/python3
"""
This module defines the add_integer function
"""


def add_integer(a, b=98):
    """
    Function to add two integers
    :param a: Number to be added
    :param b:  Number to be added
    :return: Sum of two numbers
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
