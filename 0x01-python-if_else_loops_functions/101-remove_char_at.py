#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ''
    i = 0
    if n <= len(str) and n >= 0:
        for char in str:
            if i != n:
                copy += char
            i += 1
        return (copy)
    else:
        return (str)
