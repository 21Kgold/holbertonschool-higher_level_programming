#!/usr/bin/python3
# Function that retrieves an element from a list
# Function prototype
def element_at(my_list, idx):
    # Indentated code from this point means that code
    # is part of the function

    # Check if the element to retrive it
    # is within the valid range
    # len returns the number of elements
    # Valid range goes from 0 to the last
    # index element value

    if idx < 0 or idx > len(my_list) - 1:
        return None
    # Retrive the element at the idx position

    return my_list[idx]
