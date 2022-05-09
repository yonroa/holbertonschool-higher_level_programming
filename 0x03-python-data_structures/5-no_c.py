#!/usr/bin/python3
def no_c(my_string):
    i = 0
    string = list(my_string)
    while i < len(string):
        if string[i] == "c" or string[i] == "C":
            string.pop(i)
            i = 0
        else:
            i += 1
    return ("".join(string))
