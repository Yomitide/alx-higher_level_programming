#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_c = len(argv)
    num_sum = 0

    for val in range(1, argv_c):
        num_sum += int(argv[val])
        print(num_sum)
