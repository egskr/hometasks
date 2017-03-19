#!/usr/bin/python
"""
https://www.codewars.com/kata/anything
Description:

What is the answer to life the universe and everything

Create a function that will make anything true

    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True'

"""
import re
import math
class anything(object):
    def __init__(self, ourvalue):
        pass
    def __ge__(self, ourvalue):
        return True

    def __gt__(self, ourvalue):
        return True

    def __lt__(self, ourvalue):
        return True

    def __le__(self, ourvalue):
        return True

    def __eq__(self, ourvalue):
        return True



#print(anything(re) <= re)
print(anything(95) >= 667)
