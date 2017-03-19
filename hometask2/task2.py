#!/usr/bin/python
'''
Написать скрипт, который определяет, является ли заданная строка полиндромом.
Строку можно жестко задать в коде.
'''

text = list(input("Write string: "))
text1 = text[:]  # text1 for reverse

text1.reverse()

print(text)
print(text1)

if text == text1:
    print("Polindrom")
else:
    print("NO")
