#!/usr/bin/python3

import random

number = random.randint(-10, 10)  # Generates a random integer between -10 and 10

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

