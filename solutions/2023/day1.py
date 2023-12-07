import re

from util.input import input_lines
from util.output import aoc_solve


def part_1(lines):
    return sum(int(digits[0] + digits[-1]) for digits in [re.findall(r'\d', line) for line in lines])


numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def digitize(token):
    return str(numbers.index(token)) if token in numbers else token


def part_2(lines):
    pattern = r'(?=(\d|' + r'|'.join(numbers) + '))'
    result = 0
    for line in lines:
        digits = [digitize(token) for token in re.findall(pattern, line)]
        result += int(digits[0] + digits[-1])
    return result


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day1.txt'))
    # part 1: 54338
    # part 2: 53389
