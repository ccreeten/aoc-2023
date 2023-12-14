from itertools import chain

from util.input import input_grids
from util.math import transpose
from util.output import aoc_solve


def summarize(grid, diff):
    for row in range(1, len(grid)):
        size = min(row, len(grid) - row)
        above = grid[row - size:row]
        below = grid[row:row + size]

        pairs = chain(*map(lambda rows: zip(*rows), zip(above, reversed(below))))
        if sum(l != r for l, r in pairs) == diff:
            return row
    return 0


def method_name(grid, diff):
    return summarize(grid, diff) * 100 or summarize(transpose(grid), diff)


def part_1(grids):
    return sum(method_name(grid, 0) for grid in grids)


def part_2(grids):
    return sum(method_name(grid, 1) for grid in grids)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_grids('2023/day13.txt'))
    # part 1: 27742
    # part 2: 32728
