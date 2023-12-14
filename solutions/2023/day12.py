from functools import lru_cache
from itertools import repeat

from util.input import input_lines
from util.output import aoc_solve
from util.parse import ints


@lru_cache
def count_groups(springs, si, groups, gi):
    if gi >= len(groups):
        return 0 if '#' in springs[si:] else 1
    if si >= len(springs):
        return 0

    if springs[si] == '.':
        return count_groups(springs, si + 1, groups, gi)

    count = 0
    if springs[si] == '?':
        count += count_groups(springs, si + 1, groups, gi)

    group_size = groups[gi] - 1
    si += 1
    while group_size and si < len(springs):
        if springs[si] == '.':
            break
        group_size -= 1
        si += 1

    if group_size or si < len(springs) and springs[si] == '#':
        return count

    if si < len(springs) and springs[si] == '?':
        si += 1
    return count + count_groups(springs, si, groups, gi + 1)


def analyze_records(records, unfolds):
    counts = 0
    for record in records:
        springs, groups = record.split(' ')
        springs, groups = '?'.join(repeat(springs, unfolds)), ','.join(repeat(groups, unfolds))
        springs, groups = tuple(list(springs)), tuple(ints(groups))

        x = count_groups(springs, 0, groups, 0)
        counts += x
    return counts


def part_1(lines):
    return analyze_records(lines, 1)


def part_2(lines):
    return analyze_records(lines, 5)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day12.txt'))
    # part 1: 7163
    # part 2: 17788038834112
