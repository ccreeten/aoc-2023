from util.input import input_lines
from util.output import aoc_solve
from util.parse import ints


def score(sheet):
    result = 1
    for time, distance in sheet:
        wins = 0
        for speed in range(1, time):
            travel = speed * (time - speed)
            if travel > distance:
                wins += 1
        result *= wins
    return result


def part_1(lines):
    return score(zip(ints(lines[0]), ints(lines[1])))


def part_2(lines):
    return score(zip(ints(lines[0].replace(' ', '')), ints(lines[1].replace(' ', ''))))


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day6.txt'))
    # part 1: 1660968
    # part 2: 26499773
