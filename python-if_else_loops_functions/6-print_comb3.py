#!/usr/bin/python3
for a in range(0, 8):
    for b in range(a, 10):
        if a != b:
            print("{:d}{:d}, ".format(a, b), end='')
print("89")
