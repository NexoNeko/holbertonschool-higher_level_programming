#!/usr/bin/python3


def roman_to_int(roman_string):
    c = []
    res = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in roman_string:
        for a, b in romans.items():
            if i == a:
                c.append(b)

    for i in range(len(c)):
        if i < len(c) - 1 and c[i] < c[i + 1]:
            res -= c[i]
        else:
            res += c[i]
    return res
