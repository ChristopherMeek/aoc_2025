from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int    

def parse(input: str) -> list[Coordinate]:    
    return [Coordinate(*map(int, line.split(','))) for line in input.strip().splitlines()]