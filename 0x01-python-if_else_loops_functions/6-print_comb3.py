#!/usr/bin/python3
for tenth_digit in range(0, 8):
    for unit_digit in range(tenth_digit + 1, 10):
        print("{}{}, ".format(tenth_digit, unit_digit), end='')
print('{}'.format(89))
