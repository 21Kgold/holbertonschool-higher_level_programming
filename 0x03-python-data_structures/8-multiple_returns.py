#!/usr/bin/python3
# Function that returns a tuple with the length of
# a string and its first character

def multiple_returns(sentence):

    # Check if the length of the string is an special case
    # with no data

    # The None keyword is used to define a null value, or no value at all.
    # None is not the same as 0, False, or an empty string. None is a data
    # type of its own (NoneType) and only None can be None

    if len(sentence) == 0:
        new = (0, None)
    else:

        # Retrive the string char using its index position

        new = (len(sentence), sentence[0])
    return new
