#!/usr/bin/python3

def uppercase(str):
    for char in str:
        c_char = char
        if ord(char) >= 97 and ord(char) <= 122:
            c_char = chr(ord(char) - 32)
        else:
            c_char = char
        print('{0}'.format(c_char), end='')
    print('{0}'.format('\n'))
