#!/bin/usr/python3

def check_even_odd(num):
    if num % 2 == 0:
        return "This is an even number"
    else:
        return "This is an odd number"


print(check_even_odd(5))
print(check_even_odd(24))
print(check_even_odd(19))
print(check_even_odd(4))
print(check_even_odd(215.2))
