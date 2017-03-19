#!/usr/bin/python
'''
Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не
хватило значения, в словаре должно быть значение None. Значения, которым не хватило
ключей, нужно игнорировать.
'''

spisA = ['one', 'two', 'three', 'four', 'five', 'six']
spisB = [1, 2, 3, 4]

spisAcount = len(spisA)
spisBcount = len(spisB)

if spisAcount > spisBcount:
    for _ in range(spisAcount - spisBcount):
        spisB.append('None')

mydict = dict(zip(spisA, spisB))

print(mydict)



