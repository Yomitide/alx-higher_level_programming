#!/usr/bin/python3

for alph in reversed(range(97, 123)):
    print("{}".format(chr(alph) if alph % 2 == 0 else chr(alph - 32)), end="")
