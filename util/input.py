def input_parsed(path, f):
    with open(f'../../inputs/{path}', 'r') as text:
        return f(text.read())


def input_lines(path):
    return input_parsed(path, lambda text: text.split('\n'))
