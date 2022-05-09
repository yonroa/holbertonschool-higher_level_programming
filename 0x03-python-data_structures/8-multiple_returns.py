#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return ((long, first))
