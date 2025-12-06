from .parser import parse_1, parse_2
from .solutions import part_1
from get_aoc_data import get_aoc_data

test_input = '''123 328  51 64  
 45 64  387 23  
  6 98  215 3144
*   +   *   +   '''

puzzle_input = get_aoc_data(6)

#print("Test Input Part 1 Results:", part_1(parse_1(test_input)))
#print("Puzzle Input Part 1 Results:", part_1(parse_1(puzzle_input)))

#print("Test Input Part 2 Results:", part_1(parse_2(test_input)))
print("Puzzle Input Part 2 Results:", part_1(parse_2(puzzle_input)))
