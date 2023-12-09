from util.input import input_lines
from util.output import aoc_solve
from util.parse import ints


def find_next(seq):
    if not seq:
        return 0
    return seq[-1] + find_next([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])


def part_1(lines):
    return sum(find_next(ints(seq)) for seq in lines)


def part_2(lines):
    return sum(find_next(list(reversed(ints(seq)))) for seq in lines)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day9.txt'))
    # part 1: 1904165718
    # part 2: 964
