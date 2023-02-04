#!/usr/bin/python3
"""Defines fun that prints 2 new lines after ., ? or :"""

def text_indentation(text):
"""prints 2 new lines after ., ? or :
    Removes spaces at begining of new line.
    If text is not string, throws a type error"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    spc_flag = 0
    la = []

    for i in text:
        # this removes spaces
        if spc_flag == 1:
            if i == " ":
                continue
            spc_flag = 0

        if i == "."\
                or i == "?"\
                or i == ":":
            la.append(i)
            la.append("\n\n")
            # sets flag for space removal
            spc_flag = 1
        else:
            la.append(i)

    print("".join(la))
