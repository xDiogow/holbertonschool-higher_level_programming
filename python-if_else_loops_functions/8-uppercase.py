#!/usr/bin/python3

def uppercase(str):
    end_str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print(chr(ord(char) + 32))
        else:
            print(char)
