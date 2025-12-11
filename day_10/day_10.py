from .parser import parse
from .solutions import part_1, part_2
from get_aoc_data import get_aoc_data
import pulp

test_input = '''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''

parsed_test_input = parse(test_input)
print('Test Input Part 1:', part_1(parsed_test_input))
print('Test Input Part 2:', part_2(parsed_test_input))

puzzle_input = get_aoc_data(10)
parsed_puzzle_input = parse(puzzle_input)
print('Puzzle Input Part 1:', part_1(parsed_puzzle_input))
print('Puzzle Input Part 2:', part_2(parsed_puzzle_input))