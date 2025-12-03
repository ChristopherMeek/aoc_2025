from .parser import banks_parser
from .solutions import solve
from get_aoc_data import get_aoc_data

TEST_INPUT = '''987654321111111
811111111111119
234234234234278
818181911112111'''

PUZZLE_INPUT = get_aoc_data(3)

parsed_test_input = banks_parser.parse(TEST_INPUT)
parsed_puzzle_input = banks_parser.parse(PUZZLE_INPUT)

print("Test Input Part 1 Solution:" , solve(parsed_test_input, 2))
print("Puzzle Input Part 1 Solution:", solve(parsed_puzzle_input, 2))

print("Test Input Part 2 Solution:" , solve(parsed_test_input, 12))
print("Puzzle Input Part 2 Solution:", solve(parsed_puzzle_input, 12))