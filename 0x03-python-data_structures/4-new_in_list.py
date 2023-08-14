#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    length = len(my_list)

    copy_list = my_list[:]

    if 0 <= idx < length:
        copy_list[idx] = element

    return (copy_list)
