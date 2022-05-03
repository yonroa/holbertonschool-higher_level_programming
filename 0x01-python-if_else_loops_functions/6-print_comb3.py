#!/usr/bin/python3
for i in range(0, 9):
    for h in range(i + 1, 10):
        if i == 8:
            print(f"{i}{h}")
        else:
            print(f"{i}{h}", end=", ")
