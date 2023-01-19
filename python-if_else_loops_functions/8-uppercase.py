#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            print("{:c}".format(ord(character) - 32), end = '')
        else:
            print(f"{character}", end = '')
    print("")
