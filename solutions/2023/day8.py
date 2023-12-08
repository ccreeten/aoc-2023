import math
import re
from itertools import cycle

from util.input import input_lines
from util.output import aoc_solve


def steps(graph, moves, node, ends):
    for steps, move in enumerate(cycle(moves)):
        if re.match(ends, node):
            return steps
        node = graph[node][0 if move == 'L' else 1]


def least_steps(lines, starts, ends):
    lines = iter(lines)
    moves = next(lines)
    next(lines)

    graph = {id: (l, r) for id, l, r in [re.findall(r'[A-Z0-9]{3}', line) for line in lines]}
    cycles = [steps(graph, moves, node, ends) for node in graph if re.match(starts, node)]

    return math.lcm(*cycles)


def part_1(lines):
    return least_steps(lines, r'AAA', r'ZZZ')


def part_2(lines):
    return least_steps(lines, r'..A', r'..Z')


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day8.txt'))
    # part 1: 13019
    # part 2: 13524038372771
