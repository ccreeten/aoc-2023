import re


def first_int(string):
    return int(re.search(r'\d+', string).group())


def ints(string):
    return [int(token) for token in re.findall(r'\d+', string)]
