from .parser import parse, Coordinate
from .solutions import part_1, part_2
from get_aoc_data import get_aoc_data

test_input = '''
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
'''

parsed_test_input = parse(test_input)
print("Part 1 - Test Input:", part_1(parsed_test_input))
print("Part 2 - Test Input:", part_2(parsed_test_input))

puzzle_input = get_aoc_data(9)
parsed_puzzle_input = parse(puzzle_input.strip())   
print("Part 1 - Puzzle Input:", part_1(parsed_puzzle_input))
print("Part 2 - Puzzle Input:", part_2(parsed_puzzle_input))