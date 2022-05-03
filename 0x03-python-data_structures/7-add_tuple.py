#!/usr/bin/python3
# Function that add tuples of 2 elements
# In Python tuples have parentheses and lists have brackets

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_i = (0, 0)
    elif len(tuple_a) == 1:
        tuple_i = (tuple_a[0], 0)
    else:
        tuple_i = tuple(tuple_a)

    if tuple_b == ():
        tuple_j = (0, 0)
    elif len(tuple_b) == 1:
        tuple_j = (tuple_b[0], 0)
    else:
        tuple_j = tuple(tuple_b)

    return (tuple_i[0] + tuple_j[0], tuple_i[1] + tuple_j[1])
