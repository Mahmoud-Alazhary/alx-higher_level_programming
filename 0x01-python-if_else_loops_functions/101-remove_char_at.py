#!/usr/bin/python3
def remove_char_at(str, n):
    after_removal_str = ''
    if n >= 0 and n < len(str):
        after_removal_str = str[0:n] + str[n + 1: len(str)]
        return (after_removal_str)
    else:
        return (str)
