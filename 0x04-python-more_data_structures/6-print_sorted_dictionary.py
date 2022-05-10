#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary.items())
    for i in range(0, len(order)):
        print(f"{order[i][0]}: {order[i][1]}")
