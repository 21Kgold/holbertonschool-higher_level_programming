#!/usr/bin/python3
                                # Function that retrieves an element from a list
def element_at(my_list, idx):   # Function prototype
                                # Indentated code from this point means that code
                                # is part of the function

                                            # Check if the element to retrive it
                                            # is within the valid range
    if idx < 0 or idx > len(my_list) - 1:   # len returns the number of elements
        return None                         # Valid range goes from 0 to the last
                                            # index element value

    return my_list[idx]         # Retrive the element at the idx position
