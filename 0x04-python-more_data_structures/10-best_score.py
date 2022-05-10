#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        maximus = max(a_dictionary.items())
        return (maximus[0])
    except:
        return (None)
