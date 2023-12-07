import re
from math import prod

from util.input import input_lines
from util.output import aoc_solve


def part_1(lines):
    result = 0
    for row in range(len(lines)):
        for number in re.finditer(r'\d+', lines[row]):
            for delta in [-1, 0, 1]:
                delta = row + delta
                if 0 <= delta < len(lines):
                    for special in re.finditer(r'[^\d.]', lines[delta]):
                        if special.start() >= number.start() - 1 and special.end() <= number.end() + 1:
                            result += int(number.group())
    return result


def part_2(lines):
    result = 0
    for row in range(len(lines)):
        for gear in re.finditer(r'\*', lines[row]):
            numbers = []
            for delta in [-1, 0, 1]:
                delta = row + delta
                if 0 <= delta < len(lines):
                    for number in re.finditer(r'\d+', lines[delta]):
                        if gear.start() >= number.start() - 1 and gear.end() <= number.end() + 1:
                            numbers.append(int(number.group()))
            if len(numbers) == 2:
                result += prod(numbers)
    return result


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day3.txt'))
    # part 1: 549908
    # part 2: 81166799
