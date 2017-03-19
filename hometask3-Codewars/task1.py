#!/usr/bin/python
"""
https://www.codewars.com/kata/polynomials-i-string-format/train/python
Make a function, calc_pol() that receives a polynomial like a string,
pol_str and a value of the variable x, x. The function will output the result in a string format.
If the result P(x) is 0, the function will output that x is a root of the polynomial.
"""
import ast


def calc_pol(pol_str, x=None):

        if x is None:
            return "There is no value for x"

        node = ast.parse(pol_str, mode='eval')
        code_object = compile(node, filename='<string>', mode='eval')
        res = eval(code_object)
        print(res)

        if res == 0 :
            result = "Result = {}, so {} is a root of {}".format(res, x, pol_str)
        else:
            result = "Result = {}".format(res)

        return result


print(calc_pol('2*x**2 + 3*x - 44', 4))