#!/usr/bin/python3
# Function that finds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    new = list(my_list)
    # Check if the list is a special case of empy list
    if len(my_list) == 0:
        new = None
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] % 2 != 0:
                new[i] = False
            else:
                new[i] = True
        return new
