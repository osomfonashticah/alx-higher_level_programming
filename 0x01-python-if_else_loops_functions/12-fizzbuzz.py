#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz", sep=" ", end="\n")
        elif i % 3 == 0:
            print("Fizz", sep=" ", end="\n")
        elif i % 5 == 0:
            print("Buzz", sep=" ", end="\n")
        else:
            print(i, sep=" ", end="\n")
