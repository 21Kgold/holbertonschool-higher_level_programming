#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    # Create a list with the function list
    # and fill it with the same data as my_list

    new = list(my_list)

# Check if the element to replace it
# is within the valid range, if not
# return a copy of the original list

    if idx < 0 or idx > len(my_list) - 1:
        return new

# Replace the element at the position idx
# and return the modified copied list

    new[idx] = element
    return new
