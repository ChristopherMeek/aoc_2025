from get_aoc_data import get_aoc_data
from .parser import parse
from .solutions import part_1, part_2

TEST_INPUT = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''.strip()

puzzle_input = get_aoc_data(5)

print("Test Solution Part 1:", part_1(parse(TEST_INPUT)))
print("Puzzle Solution Part 1:", part_1(parse(puzzle_input)))


print("Test Solution Part 2:", part_2(parse(TEST_INPUT)[0]))
print("Puzzle Solution Part 2:", part_2(parse(puzzle_input)[0]))