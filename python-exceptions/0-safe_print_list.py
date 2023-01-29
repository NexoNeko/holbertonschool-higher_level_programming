#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    pid = 0
    try:
        for i in my_list:
            if pid < x:
                print('{}'.format(my_list[pid]), end='')
                pid += 1
        print()
    except TypeError:
        pass
    finally:
        return pid
