#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print('{0}'.format(chr(ord(char) - 32)), end='')
        else:
            print('{0}'.format(char), end='')
    print('{0}'.format('\n'))
