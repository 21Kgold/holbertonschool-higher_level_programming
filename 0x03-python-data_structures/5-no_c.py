#!/usr/bin/python3
def no_c(my_string):

    # Function that removes all characters c and C from a string
    # Create a new, empty string

    new = ""

    # Evaluate each character of my_string to
    # filter c and C

    for i in my_string:
        if i != "c" and i != "C":

            # Add filtered data in the new string
            # Return the new string

            new += i
    return new
