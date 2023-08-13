#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    argv_c = len(sys.argv) - 1
    if argv_c != 3:
        print("usage: ./calculator.py <a> <operator> <b>")
    sys.exit(1)

    a = int(input("enter a number"))
    b = int(input("enter a number"))
    operator = input("enter an operator:+, -, *, /")
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: {operator}\n")
        exit(1)
