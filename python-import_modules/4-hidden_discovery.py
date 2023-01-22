#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    stuff = dir(hidden_4)
    for i in stuff:
        if i[:2] != "__":
            print(i)
