#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 1:
        a = "argument:"
    elif len(sys.argv) - 1 == 0:
        a = "arguments."
    else:
        a = "arguments:"
    print("{} {}".format(len(sys.argv) - 1, a))

    for b in range(len(sys.argv) - 1):
        print("{}: {}".format(b + 1, sys.argv[b + 1]))
