#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maximus = 0
        for number in my_list:
            if number > maximus:
                maximus = number
        return (maximus)
    else:
        return (None)
