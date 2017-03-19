#!/usr/bin/python
"""
https://www.codewars.com/kata/ipv4-validator
Description:

In this kata you have to write a method to verify the validity of IPv4 addresses.

Example of valid inputs:

"1.1.1.1"

"127.0.0.1"

"255.255.255.255"

Example of invalid input:

"1444.23.9"

"153.500.234.444"

"-12.344.43.11"

"""
def ipValidator(ip):
    if len(ip.split('.')) != 4 or ip.count(' ') > 0 :
        return False
    for i in ip.split('.'):
        try:
          if int(i) < 0 or int(i) > 255:
              return False
        except ValueError:
            return False
    return True



print(ipValidator('127.0.0.1'))