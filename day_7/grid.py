from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y'])

class Grid:
    def __init__(self, data: str):
        self.grid = [list(line) for line in data.strip().splitlines()]
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.height > 0 else 0
    
    def print_grid(self):
        print(f"Grid ({self.width}x{self.height})")
        for row in self.grid:
            print(''.join(row))

    def find(self, char: str) -> Coordinate:
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == char:
                    return Coordinate(x, y)
        return None
    
    def at(self, coord: Coordinate) -> str:
        if 0 <= coord.x < self.width and 0 <= coord.y < self.height:
            return self.grid[coord.y][coord.x]
        return None
    
    def set_at(self, coord: Coordinate, value: str):
        if 0 <= coord.x < self.width and 0 <= coord.y < self.height:
            self.grid[coord.y][coord.x] = value