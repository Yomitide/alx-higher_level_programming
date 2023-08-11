#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = 0

if number < 0:
    number = number * -1
    lastDigit = (number % 10) * -1
    number = number * -1
else:
    lastDigit = number % 10

print(f'Last digit of {number} is {lastDigit}', end=" ")

if lastDigit < 6 and lastDigit != 0:
    print(f'and is less than 6 and not 0')
elif lastDigit > 5:
    print(f'and is greater than 5')
else:
    print(f'and is 0')
