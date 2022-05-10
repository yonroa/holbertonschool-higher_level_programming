#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    maximus = max(a_dictionary.items())
    return (maximus[0])
