#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

if len(argv) != 3:
    print(f"{a} {operator} {b}\n")
    exit(1)

    a = int(input("enter a number"))
    b = int(input("enter a number"))
    operator = input("enter an operator:+, -, *, /")
    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.sub(a, b)
    elif operator == "*":
        result = calculator_1.mul(a, b)
    elif operator == "/":
        result = calculator_1.div(a, b)
    else:
        print(f"Unknown operator. Available operators: {operator}\n")
        exit(1)

        print("{a} {operator} {b} = {result}".format(a, operator, b, operator(result)))
