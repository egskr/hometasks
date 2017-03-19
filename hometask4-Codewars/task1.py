#!/usr/bin/python
"""
https://www.codewars.com/kata/fractions-class/
Description:
You are provided with a skeleton of the class 'Fraction', which accepts two arguments (numerator, denominator).
EXAMPLE:
fraction1 = Fraction(4, 5)
Your task is to make this class string representable, and addable while keeping the result in the minimum representation possible.
EXAMPLE:
print (fraction1 + Fraction(1, 8))
outputs: 37/40
NB: DON'T use the built_in class 'fractions.Fraction'
"""




class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    #Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, addfract):
        numeratorX = self.top * addfract.bottom + self.bottom * addfract.top
        denominatorX = self.bottom * addfract.bottom
        for i in range(min(numeratorX, denominatorX), 1, -1):
            if (numeratorX % i == 0) and (denominatorX % i == 0):
                numeratorX /= i
                denominatorX /= i
        return Fraction(int(numeratorX), int(denominatorX))