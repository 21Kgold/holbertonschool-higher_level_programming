#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    # First, check for special case when list is empty

    if my_list is None or my_list == ():
        return None
        # i range go from 0 inclusive to len exclusive
    else:
        for i in range(len(my_list)):
            print(my_list[-1 - i])
