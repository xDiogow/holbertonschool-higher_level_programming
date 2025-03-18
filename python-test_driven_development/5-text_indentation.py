#!/usr/bin/python3
"""
This module is used for text indentation
"""

def text_indentation(text):
    """
    Prints each line of text by adding an empty line
    :param text: Text to be indented
    :return: None
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')


    for line in text.splitlines():
        print(line)
