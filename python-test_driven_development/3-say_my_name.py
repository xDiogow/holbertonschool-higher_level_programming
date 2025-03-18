#!/usr/bin/python3
"""
This module defines a function that prints a name.
"""

def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}", end='')