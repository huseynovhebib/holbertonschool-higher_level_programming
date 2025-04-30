#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Check if the character is a lowercase letter
            print(chr(ord(char) - 32), end="")  # Convert lowercase to uppercase
        else:
            print(char, end="")  # Print non-lowercase characters as they are
    print()  # Print the new line at the end

