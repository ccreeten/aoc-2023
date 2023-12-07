from util.input import input_lines
from util.output import aoc_solve
from util.parse import ints


def part_1(lines):
    lines = iter(lines)
    seeds = ints(next(lines))

    next(lines)
    while next(lines, None):
        mapping = []
        while map := next(lines, None):
            mapping.append(ints(map))
        for i in range(len(seeds)):
            for destination, source, length in mapping:
                if source <= seeds[i] < source + length:
                    seeds[i] = seeds[i] - source + destination
                    break
    return min(seeds)


def part_2(lines):
    lines = iter(lines)
    seeds = iter(ints(next(lines)))
    need_mapped = list(zip(seeds, seeds))

    next(lines)
    while next(lines, None):
        mapping = []
        while map := next(lines, None):
            mapping.append(ints(map))
        mapping.sort(key=lambda m: m[1])

        have_mapped = []
        while need_mapped:
            work = []
            for start, n_len in need_mapped:
                for destination, source, m_len in mapping:
                    s_end = source + m_len
                    if source <= start < s_end or source < start + n_len <= s_end:
                        h_start = destination + (start - source)
                        h_len = min(n_len, destination + m_len - h_start)
                        have_mapped.append((h_start, h_len))
                        if start < source:
                            work.append((start, source - start))
                        if start + n_len > s_end:
                            work.append((s_end, n_len - h_len))
                        break
                else:
                    have_mapped.append((start, n_len))
            need_mapped = work
        need_mapped = have_mapped
    return min(start for start, _ in need_mapped)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day5.txt'))
    # part 1: 510109797
    # part 2: 9622622
