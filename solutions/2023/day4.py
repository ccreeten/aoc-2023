from util.input import input_lines
from util.output import aoc_solve
from util.parse import ints


def parse_cards(lines):
    for line in lines:
        _, numbers = line.split(':')
        winning, have = numbers.split('|')
        yield ints(winning), ints(have)


def part_1(lines):
    result = 0
    for winning, have in parse_cards(lines):
        if intersection := set(winning).intersection(have):
            result += 2 ** (len(intersection) - 1)
    return result


def part_2(lines):
    copies = {card: 1 for card in range(len(lines))}
    for card, (winning, have) in enumerate(parse_cards(lines)):
        for idx in range(len(set(winning).intersection(have))):
            copies[card + idx + 1] += copies[card]
    return sum(copies.values())


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day4.txt'))
    # part 1: 21485
    # part 2: 11024379
