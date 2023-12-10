def exists(grid, pos):
    row, col = pos
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def get(grid, pos):
    row, col = pos
    return grid[row][col]


def positions(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            yield row, col
