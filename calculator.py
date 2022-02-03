"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True: 
    user__user = input("Enter your operation: ")
    x = int(input("Enter you first number:"))
    y = int(input("Enter your second number:"))
    tokens = [user__user, x, y]
    if tokens[0] == 'pow': 
        print(float(power(tokens[1], tokens[2])))
    elif tokens[0] == 'square':
        print(float(square(tokens[1])))
    elif tokens[0] == 'add': 
        print(float(add(tokens[1], tokens[2])))
    elif tokens[0] == 'subtract':
        print(float(subtract(tokens[1], tokens[2])))
    elif tokens[0] == 'multiply':
        print(float(multiply(tokens[1], tokens[2])))
    elif user__user == 'q':
        break
# Replace this with your code

