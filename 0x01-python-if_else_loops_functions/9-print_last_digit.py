#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = 0
    if number < 0:
        number *= -1

    lastDigit = number % 10

    print(lastDigit, end="")
    return lastDigit
