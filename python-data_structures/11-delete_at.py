#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            continue
        new_list.append(my_list[i])
    my_list = new_list
    return new_list
