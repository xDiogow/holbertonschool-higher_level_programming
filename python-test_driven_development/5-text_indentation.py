#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')


    for line in text.splitlines():
        print(line)