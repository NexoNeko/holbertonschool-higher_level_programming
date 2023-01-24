#!/usr/bin/python3
import sys


if __name__ == "__main__":
    arg_num = len(sys.argv)

    if arg_num == 1:
        print("0 arguments.")
    elif arg_num == 2:
        print("{} argument:".format(arg_num - 1))
    else:
        print("{} arguments:".format(arg_num - 1))

    for i in range(1, arg_num):
        print("{}: {}".format(i, sys.argv[i]))
