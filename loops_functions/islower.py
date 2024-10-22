#!/usr/bin/python
def islower(c):
    if len(c) == 1:
        return c.islower()
    return False

print(islower('a'))
print(islower('A'))
print(islower('1'))
print(islower('abc'))
