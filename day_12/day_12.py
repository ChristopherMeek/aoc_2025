from .parser import parse
from .solutions import sanity_check
from get_aoc_data import get_aoc_data

test_input = '''
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
'''

puzzle_input = get_aoc_data(12)

parsed_test_input = parse(test_input.strip())
parsed_puzzle_input = parse(puzzle_input)

print("Test input sanity check:", sanity_check(parsed_test_input))

# This is one of those cases where the test input is harder to solve than the actual puzzle input
# because the puzzle input has much more generous tree sizes.
# the present either fir with a lot of spare space or they don't fit at all.
# this stupid sanity check is enough to solve the puzzle input.
print("Puzzle input sanity check:", sanity_check(parsed_puzzle_input))