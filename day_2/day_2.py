from get_aoc_data import get_aoc_data
from .parser import ranges_parser
from .solutions import part_1, part_2

test_input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
puzzle_input = get_aoc_data(2)

parsed_test_input = ranges_parser.parse(test_input)
parsed_puzzle_input = ranges_parser.parse(puzzle_input)

print("Test Input Results:", part_1(parsed_test_input))
print("Puzzle Input Results:", part_1(parsed_puzzle_input))

print("Test Input Part 2 Results:", part_2(parsed_test_input))
print("Puzzle Input Part 2 Results:", part_2(parsed_puzzle_input))