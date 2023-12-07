from collections import Counter

from util.input import input_lines
from util.output import aoc_solve


def solve(lines, alphabetize, score):
    plays = []
    for hand, bid in map(lambda line: line.split(), lines):
        plays.append((alphabetize(hand), int(bid)))

    plays.sort(key=lambda play: play[0])
    plays.sort(key=lambda play: score(play[0]))

    return sum((idx + 1) * plays[idx][1] for idx in range(len(plays)))


def alphabetize(hand):
    cards = ['A', 'K', 'Q', 'J', 'T'] + [str(digit) for digit in reversed(range(2, 10))]
    return ''.join(chr(ord('z') - cards.index(card)) for card in hand)


def type_value(hand):
    counts = Counter(hand)
    match len(counts):
        case 1: return 7
        case 2: return 6 if 1 in counts.values() else 5
        case 3: return 4 if 3 in counts.values() else 3
        case 4: return 2
        case 5: return 1


def part_1(lines):
    return solve(lines, alphabetize, type_value)


def alphabetize_part_2(hand):
    cards = ['A', 'K', 'Q', 'T'] + [str(digit) for digit in reversed(range(2, 10))] + ['J']
    return ''.join(chr(ord('z') - cards.index(card)) for card in hand)


def joker_value(hand):
    cards = [chr(card) for card in range(ord('z') + 1)]
    return max(type_value(hand.replace('n', card)) for card in cards)


def part_2(lines):
    return solve(lines, alphabetize_part_2, joker_value)


if __name__ == '__main__':
    aoc_solve(part_1, part_2, input_lines('2023/day7.txt'))
    # part 1: 251121738
    # part 2: 251421071
