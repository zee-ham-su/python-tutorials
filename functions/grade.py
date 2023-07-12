#!/bin/usr/python3
import sys

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"


# Check if a command-line argument is provided
if len(sys.argv) > 1:
    marks = int(sys.argv[1])  # Get the marks from the command-line argument
    result = grade(marks)     # Call the grade function
    print("Grade:", result)   # Print the grade
