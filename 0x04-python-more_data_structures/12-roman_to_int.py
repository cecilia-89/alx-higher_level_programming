#!/usr/bin/python3

def roman_to_int(roman_string):

    if isinstance(roman_string, str):
        roman = {
        'I': 1, 'IV': 4, 'V': 5,
        'XI': 9, 'X': 10, 'XL': 40,
        'L': 50, 'C': 100, 'D': 500,
        }

        res = [roman[i] for i in roman_string]
        return sum(res)

    return 0
