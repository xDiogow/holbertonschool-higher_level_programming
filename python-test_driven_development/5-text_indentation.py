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

    lines = []
    for line in text.split('\n'):
        stripped_line = line.strip()
        lines.append(stripped_line)

    print("\n".join(lines), end="")
