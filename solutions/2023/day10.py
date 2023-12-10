from util.grid import positions
from util.input import input_grid
from util.output import aoc_solve

deltas = {
    '|': [(-1, +0), (+1, +0)],
    '-': [(+0, -1), (+0, +1)],
    'L': [(-1, +0), (+0, +1)],
    'J': [(-1, +0), (+0, -1)],
    '7': [(+1, +0), (+0, -1)],
    'F': [(+1, +0), (+0, +1)],
    'S': [[+1, +0], (-1, +0), (+0, +1), (+1, -1)],
}


def get_loop(grid, pr, pc, r, c, path):
    if grid[r][c] == 'S' and [pr, pc] != [r, c]:
        return path

    for dr, dc in deltas[grid[r][c]]:
        nr, nc = r + dr, c + dc
        if nr == pr and nc == pc:
            continue
        path.add((r, c))
        return get_loop(grid, r, c, nr, nc, path)


def part_1(grid):
    for row, col in positions(grid):
        if grid[row][col] == 'S':
            path = get_loop(grid, row, col, row, col, set())
            return len(path) // 2


def encapsulated_count(grid, path, row):
    if row == len(grid):
        return 0

    prev, count, inside = '', 0, False
    for col in range(len(grid[row])):
        if (row, col) in path:
            cur = grid[row][col]
            if cur == '|' or prev + cur in ['L7', 'FJ']:
                inside = not inside
            if cur != '-':
                prev = cur
        elif inside:
            count += 1

    return count + encapsulated_count(grid, path, row + 1)


def part_2(grid):
    for row, col in positions(grid):
        if grid[row][col] == 'S':
            path = get_loop(grid, row, col, row, col, set())
            return encapsulated_count(grid, path, 0)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_grid('2023/day10.txt'))
    # part 1: 6754
    # part 2: 567
