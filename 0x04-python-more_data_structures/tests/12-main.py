#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "MMCDXXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "None"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "UNO"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
