from .parser import parse
from .solutions import part_1, part_2
from get_aoc_data import get_aoc_data

test_input = '''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''

test_input_part_2 = '''
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
'''

parsed_test_input = parse(test_input.strip())
print('Test Input Part 1 Result:', part_1(parsed_test_input))
print('Test Input Part 2 Result:', part_2(parse(test_input_part_2.strip()), "test_data.png"))    
      
puzzle_input = get_aoc_data(11)
parsed_puzzle_input = parse(puzzle_input.strip())
print('Puzzle Input Part 1 Result:', part_1(parsed_puzzle_input))
print('Puzzle Input Part 2 Result:', part_2(parsed_puzzle_input, "puzzle_data.png"))