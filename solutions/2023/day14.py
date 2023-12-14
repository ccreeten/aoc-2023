from util.grid import exists, positions, hash_grid
from util.input import input_grid
from util.output import aoc_solve


def cycle(grid, tilts):
    for dr, dc in tilts:
        for row in range(len(grid)) if dr == -1 else reversed(range(len(grid))):
            for col in range(len(grid[row])) if dc == -1 else reversed(range(len(grid[row]))):
                if grid[row][col] == 'O':
                    cr, cc = row, col
                    nr, nc = row + dr, col + dc
                    while exists(grid, (nr, nc)) and grid[nr][nc] == '.':
                        grid[cr][cc] = '.'
                        grid[nr][nc] = 'O'
                        cr, cc = nr, nc
                        nr, nc = nr + dr, nc + dc


def method_name(grid, cycles, tilts):
    loop_start, loop_cycles = 0, cycles

    seen = {}
    for iteration in range(cycles):
        cycle(grid, tilts)
        key = hash_grid(grid)
        if key in seen:
            loop_start, loop_cycles = seen[key], iteration - seen[key]
            break
        seen[key] = iteration

    for _ in range((cycles - loop_start) % loop_cycles - 1):
        cycle(grid, tilts)

    return sum(len(grid) - row for row, col in positions(grid) if grid[row][col] == 'O')


def part_1(grid):
    return method_name(grid, 1, [
        [-1, 0],
    ])


def part_2(grid):
    return method_name(grid, 1000000000, [
        [-1, 0],
        [0, -1],
        [+1, 0],
        [0, +1],
    ])


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_grid('2023/day14.txt'))
    # part 1: 106186
    # part 2: 106390
