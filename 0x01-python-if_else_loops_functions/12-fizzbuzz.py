#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz ", end="")
                continue
            else:
                print(" ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i == 100:
            print("{:d} ".format(i))
        else:
            print("{:d} ".format(i), end="")
