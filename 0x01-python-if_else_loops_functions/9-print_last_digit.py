#!/usr/bin/python3
def print_last_digit(number):
    string_number = str(number)
    print(f'{int(string_number[-1]):d}', end='')
    return (string_number[-1])
