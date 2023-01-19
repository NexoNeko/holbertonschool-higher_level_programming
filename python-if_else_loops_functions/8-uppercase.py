#!/usr/bin/python3
def uppercase(str):
    i = 0
    for character in str:
        i += 1;
        endchar = '\n' if i == (len(str)) else ""
        if ord(character) >= 97 and ord(character) <= 122:
            print("{:c}".format(ord(character) - 32), end = endchar)
        else:
            print(f"{character}", end = endchar)
