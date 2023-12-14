import copy
import sys


def print_solution(n, result):
    print(f'# part {n}: {result}')


def aoc_solve(part_1, part_2, input):
    sys.setrecursionlimit(1337 * 1337)
    print_solution(1, (part_1(copy.deepcopy(input))))
    print_solution(2, (part_2(copy.deepcopy(input))))
