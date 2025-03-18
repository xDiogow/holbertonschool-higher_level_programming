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

    for char in '.?:':
        text = text.replace(char, f'{char}\n')

    for line in text.split('\n'):
        print(line)
