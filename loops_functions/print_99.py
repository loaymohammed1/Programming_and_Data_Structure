#!/usr/bin/python
for i in range(0, 100, 10):
    for j in range(10):
        if j == 9:
            print(f"{i + j:02}", end="")
        else:
            print(f"{i + j:02}, ", end=" ")
        print()
