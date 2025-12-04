def parse_grid(input_str: str) -> dict[tuple[int, int], str]:    
    grid = {}
    lines = input_str.split('\n')
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[(x, y)] = char
    
    return grid