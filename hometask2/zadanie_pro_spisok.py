#!/usr/bin/python
# Vyvesti chislo unikal'nykh elementov spiska

a = [10, 0, 1, 2, 1, 10, 2, 3, 5, 6]

spis = []  # dlya isklyucheniya dubliruyuschihsya zapisei pro element
for _ in range(len(a)):
    if a[_] not in spis:
        print("Element {} vstrechaetsya {} raz".format(a[_], a.count(a[_])))
        spis.append(a[_])