import sys
sys.path.append('..')
from get_aoc_data import get_aoc_data
from parser import moves_parser
from count_zero_returns import count_zero_returns
from count_zero_passes import count_zero_passes

input = get_aoc_data(1)
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

result = moves_parser.parse(input)
zero_returns = count_zero_returns(result)
print(f"Dial returned to zero {zero_returns} times.")

zero_passes = count_zero_passes(result)
print(f"Dial passed through zero {zero_passes} times.")
