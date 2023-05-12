#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    count = len(sys.argv) - 1
    if count == 1:
        sum = sum
    else:
        for i in range(count):
            sum += int(sys.argv[i + 1])
    print(sum)
