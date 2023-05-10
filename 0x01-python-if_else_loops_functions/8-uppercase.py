#!/usr/bin/python3
def conversion(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)


def uppercase(string):
    newString = ""
    for char in string:
        newString += "%c" % conversion(char)
    print("{:s}".format(newString))
