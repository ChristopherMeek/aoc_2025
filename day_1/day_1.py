from get_aoc_data import get_aoc_data
from .parser import moves_parser
from .solutions import count_zero_returns, count_zero_passes

puzzle_input = get_aoc_data(1)
test_input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

parsed_test_input = moves_parser.parse(test_input)

print("Test Input Results:")
print(f"Dial returned to zero {count_zero_returns(parsed_test_input)} times.")
print(f"Dial passed through zero {count_zero_passes(parsed_test_input)} times.")
    
parsed_input = moves_parser.parse(puzzle_input)

print("Puzzle Input Results:")
print(f"Dial returned to zero {count_zero_returns(parsed_input)} times.")
print(f"Dial passed through zero {count_zero_passes(parsed_input)} times.")
