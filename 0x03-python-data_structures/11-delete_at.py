#!/usr/bin/python3
# Function that deletes the item at a specific position in a list

def delete_at(my_list=[], idx=0):
    # Check if the element to delete it is within the valid range

    if idx >= 0 and idx <= len(my_list) - 1:
        to_remove = my_list[idx]
        my_list.remove(to_remove)
    return my_list
