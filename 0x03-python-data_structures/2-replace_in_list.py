#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    # Check if the element to replace it
    # is within the valid range, if not
    # return the original list

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    # replace the element at the position idx
    # return the modified list

    my_list[idx] = element
    return my_list
