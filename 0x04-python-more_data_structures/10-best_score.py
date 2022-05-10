#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    maximus = max(a_dictionary.items())
    return (maximus[0])
