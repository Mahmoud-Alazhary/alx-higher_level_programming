#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print('{:c}'.format(ord(str[i]) - 32), end='', sep='')
        else:
            print('{}'.format(str[i]),'\n' if i == len(str) - 1 else '', end='', sep='')
