#!/usr/bin/python3
"""Module for roman_to_int"""


def roman_to_int(roman_string: str):
    """Converts a Roman numeral to an integer."""
    if roman_string is None or type(roman_string) is not str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    rep = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]

    return rep
