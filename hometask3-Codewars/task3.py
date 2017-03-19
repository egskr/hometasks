#!/usr/bin/python
"""
https://www.codewars.com/kata/reverser/train/python
Impliment the reverse function, which takes in input n and reverses it.
For instance, reverse(123) should return 321.
 You should do this without converting the inputted number into a string.
"""

def reverse(num):
    rev = 0
    while num > 0:
        rev = (10 * rev) + num % 10
        num //= 10
    return rev

print(reverse(123))
