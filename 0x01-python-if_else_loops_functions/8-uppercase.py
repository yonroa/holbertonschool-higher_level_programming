#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            c = chr(ord(char) - 32)
        else:
            c = char
        print(f"{c}", end = "")
    print("")
