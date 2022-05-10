#!/usr/bin/python3
def roman_to_int(roman_string):
    try:
        sums = []
        romans = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        spartans = list(roman_string)
        for i in range(0, len(spartans) - 1):
            if romans.get(spartans[i]) >= romans.get(spartans[i + 1]):
                sums.append(romans.get(spartans[i]))
            else:
                sums.append(-(romans.get(spartans[i])))
        sums.append(romans.get(spartans[-1]))
        return (sum(sums))
    except:
        return (0)
