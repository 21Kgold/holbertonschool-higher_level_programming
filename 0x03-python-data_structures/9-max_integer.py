#!/usr/bin/python3
# Function that finds the biggest integer of a list

def max_integer(my_list=[]):
    # Check if the list is a special case of empy list
    if len(my_list) == 0:
        maximo = None
    else:
        # Set max as the first element of the list
        maximo = my_list[0]
        # Compare each element of the list with the settled value of maximo
        for element in my_list:
            # Update the value of maximo when necessary
            if maximo < element:
                maximo = element
    return maximo
