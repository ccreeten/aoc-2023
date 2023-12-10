import re


def first_int(string):
    return ints(string)[0]


def ints(string):
    return [int(token) for token in re.findall(r'[+-]?\d+', string)]
