#!/usr/bin/python
"""
https://www.codewars.com/kata/sum-of-numbers-from-0-to-n
We want to generate a function that computes the series starting from 0 and ending until the given number following the sequence:

0 1 3 6 10 15 21 28 36 45 55 ....

which is created by

0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4, 0+1+2+3+4+5, 0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7 etc..

Input:

LastNumber

Output:

series and result
"""


def show_sequence(chislo):
    stroka = ""
    summa = 0
    if chislo >= 0:
        for i in range(chislo + 1):
            stroka += str(i) + "+"
            summa += i
        if summa == 0:
            return stroka[0:-1] + "=" + str(summa)

        return stroka[0:-1] + " = " + str(summa)
    else:
        return "{}<0".format(chislo)


print(show_sequence(50))

