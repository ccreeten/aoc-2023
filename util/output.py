def print_solution(n, result):
    print(f'# part {n}: {result}')


def aoc_solve(part_1, part_2, input):
    print_solution(1, part_1(input))
    print_solution(2, part_2(input))
