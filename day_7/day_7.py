import time

from get_aoc_data import get_aoc_data
from .grid import Grid
from .solutions import part_1, part_2

test_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

time_start = time.perf_counter()
test_grid_1 = Grid(test_input)
time_end = time.perf_counter()
print(f"Part 1, Test Input: {part_1(test_grid_1)} in {time_end - time_start:.6f}s")

time_start = time.perf_counter()    
test_grid_2 = Grid(test_input)
time_end = time.perf_counter()
print(f"Part 2, Test Input: {part_2(test_grid_2)} in {time_end - time_start:.6f}s")

time_start = time.perf_counter()
puzzle_input = get_aoc_data(7)
time_end = time.perf_counter()
print(f"Data retrieval: {time_end - time_start:.6f}s")

time_start = time.perf_counter()
puzzle_grid_1 = Grid(puzzle_input)
time_end = time.perf_counter()
print(f"Part 1, Puzzle Input: {part_1(puzzle_grid_1)} in {time_end - time_start:.6f}s")

time_start = time.perf_counter()
puzzle_grid_2 = Grid(puzzle_input)
time_end = time.perf_counter()
print(f"Part 2, Puzzle Input: {part_2(puzzle_grid_2)} in {time_end - time_start:.6f}s")