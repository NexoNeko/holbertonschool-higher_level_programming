#!/usr/bin/python3
"""Defines fun that prints 2 new lines after ., ? or :"""

def text_indentation(text):

    if type(text) is not str:
        raise TypeError("text must be a string")

    la = []
    for i in text:
        if i == "."\
                or i == "?"\
                or i == ":":
            la.append(i)
            la.append("\n\n")
        else:
            la.append(i)

    for i in range(len(la)):
        iplus = i - 1
        if la[i] == " "\
                and la[iplus] == '\n':
            la.pop(i)

    print("".join(la))
