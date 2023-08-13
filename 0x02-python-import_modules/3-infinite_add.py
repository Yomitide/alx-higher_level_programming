#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_c = len(argv)
    numbers_sum = 0

    for val in range(1, argv_c):
        numbers_sum += int(argv[val])
        print(numbers_sum)
