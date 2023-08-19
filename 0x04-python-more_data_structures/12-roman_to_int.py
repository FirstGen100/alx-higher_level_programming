#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    prev_char = 0
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)
        if value < prev_char:
            result -= value
        else:
            result += value
        prev_char = value
    return (result)
