#!/usr/bin/python
print('''
Написать скрипт, который определяет, является ли заданная строка полиндромом.
Строку можно жестко задать в коде.
''')

text = input("Write string: ")
text1 = text  # text1 for reverse
text = list(text)
text1 = list(text1)
text1.reverse()

print(text)
print(text1)

if text == text1:
    print("Polindrom")
else:
    print("NO")
