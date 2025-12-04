from get_aoc_data import get_aoc_data
from .parser import parse_grid
from .solutions import part_1, part_2

TEST_INPUT = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''.strip()

PUZZLE_INPUT = get_aoc_data(4)

if __name__ == "__main__":
    test_grid = parse_grid(TEST_INPUT)
    print(f"Test Solution Part 1: {part_1(test_grid)} accessible rolls")
    print(f"Test Solution Part 2: {part_2(test_grid)} accessible rolls")


    puzzle_grid = parse_grid(PUZZLE_INPUT)
    print(f"Puzzle Solution Part 1: {part_1(puzzle_grid)} accessible rolls")
    print(f"Puzzle Solution Part 2: {part_2(puzzle_grid)} accessible rolls")