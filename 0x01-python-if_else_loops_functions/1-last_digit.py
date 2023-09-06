#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
print('Last digit of', number, 'is', string_number[-1], end='')
if string_number[-1] > '5':
    print('and is greater than 5')
elif string_number[-1] == '0':
    print('and is 0')
elif int(string_number[-1]) < 6 and int(string_number[-1]) != 0:
    print('and is less than 6 and not 0')
