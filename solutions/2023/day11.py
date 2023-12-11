from itertools import combinations

from util.grid import positions
from util.input import input_grid
from util.math import transpose
from util.output import aoc_solve


def expand(grid, nodes, scale, component):
    empties = [i for i, row in enumerate(grid) if '#' not in row]
    for node in nodes:
        multiplier = sum(1 for i in empties if i < node[component])
        node[component] += (scale - 1) * multiplier


def expanded_distance(grid, scale):
    nodes = [[row, col] for row, col in positions(grid) if grid[row][col] == '#']

    expand(grid, nodes, scale, 0)
    expand(transpose(grid), nodes, scale, 1)

    return sum(abs(n1[0] - n2[0]) + abs(n1[1] - n2[1]) for n1, n2 in combinations(nodes, 2))


def part_1(grid):
    return expanded_distance(grid, 2)


def part_2(grid):
    return expanded_distance(grid, 1000000)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_grid('2023/day11.txt'))
    # part 1: 10276166
    # part 2: 598693078798
