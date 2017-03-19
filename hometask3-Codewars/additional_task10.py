#!/usr/bin/python
"""
https://www.codewars.com/kata/debug-the-functions-easy
Should be easy, begin by looking at the code. Debug the code and the functions should work.

There are three functions:
Multiplication (x)
Addition (+)
and
Reverse (!esreveR)
"""

def multi(l_st):
    sum = 1
    print(len(l_st))
    for i in range(len(l_st)):
        sum *= l_st[i]
    return sum

def add(l_st):
    sum = 0
    print(len(l_st))
    for i in range(len(l_st)):
        sum += l_st[i]
    return sum
def reverse(string):
    return string[::-1]


#print((reverse([8, 2, 5]), 80))
print(reverse("Hello World"),"dlroW olleH")