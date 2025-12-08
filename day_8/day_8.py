from get_aoc_data import get_aoc_data
from .parser import parse
from .solutions import part_1, part_2

test_input = '''
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
'''

parsed_test_input = parse(test_input)
print(f'Part 1 result: {part_1(parsed_test_input, 10)}')
print(f'Part 2 result: {part_2(parsed_test_input)}')

parsed_puzzle_input = parse(get_aoc_data(8))
print(f'Part 1 result: {part_1(parsed_puzzle_input, 1000)}')
print(f'Part 2 result: {part_2(parsed_puzzle_input)}')