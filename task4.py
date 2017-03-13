#!/usr/bin/python
print('''
Предположим, у нас есть access.log веб­сервера. Нужно написать скрипт, который найдет
десять IP­адресов, от которых было больше всего запросов.
''')

import os
from collections import Counter

filename = input("Enter file name [default: access.log]\n")
if not filename:
    filename = "access.log"

ipArray = []
if os.path.exists(filename):
    with open(filename, 'r') as read_file:
        for line in read_file:
            ipArray.append(((line.split('-'))[0]).strip())

    for _ in Counter(ipArray).most_common(10):
        print("IP {} vstrechaetsya {} raz".format(_[0], _[1]))

else:
    print("No such file in dir {}. Try arain".format(os.path.abspath(os.curdir)))
