import re

from util.input import input_lines
from util.output import aoc_solve
from util.parse import first_int

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def is_reveal_possible(bag, reveal):
    for colour in bag:
        if found := re.search(fr'(\d+) {colour}', reveal):
            if int(found.group(1)) > bag[colour]:
                return False
    return True


def part_1(lines):
    result = 0
    for line in lines:
        game, reveals = line.split(':')
        reveals = reveals.split(';')

        if all(is_reveal_possible(bag, reveal) for reveal in reveals):
            result += first_int(game)
    return result


def part_2(lines):
    result = 0
    for line in lines:
        power = 1
        for colour in bag:
            cubes = re.findall(fr'(\d+) {colour}', line)
            power *= max(map(int, cubes))
        result += power
    return result


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day2.txt'))
    # part 1: 2720
    # part 2: 71535
