#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbers_sum = 0

    for argv_c in sys.argv:
        if argv_c != sys.argv[0]:
            numbers_sum += int(argv_c)
            print(numbers_sum)
