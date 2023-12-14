def input_parsed(path, f):
    with open(f'../../inputs/{path}', 'r') as text:
        return f(text.read())


def input_lines(path):
    return input_split_on(path, '\n')


def input_grid(path):
    return list(map(list, input_lines(path)))


def input_grids(path):
    return list(map(lambda grid: list(map(list, grid.split('\n'))), input_split_on(path, '\n\n')))


def input_split_on(path, split_on):
    return input_parsed(path, lambda text: text.split(split_on))
