from typing import NamedTuple

class Coordinate(NamedTuple):
    x: int
    y: int
    z: int
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z       

def parse(input: str) -> set[Coordinate]:    
    return {Coordinate(*map(int, line.split(','))) for line in input.strip().splitlines()}