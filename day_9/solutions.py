from .parser import Coordinate
from itertools import combinations
from shapely.geometry.polygon import Polygon

def part_1(red_tiles: list[Coordinate]) -> int:
    areas = sorted([(abs(first.x - second.x)+1) * (abs(first.y - second.y)+1) for first, second in combinations(red_tiles, 2)], reverse=True)
    
    return areas[0]

def part_2(red_tiles: list[Coordinate]) -> int:
    p = Polygon(red_tiles)
    
    max_area = 0
    for i, tile in enumerate(red_tiles):
        for j, other_tile in enumerate(red_tiles[:i]):
            area = (abs(tile.x - other_tile.x)+1) * (abs(tile.y - other_tile.y)+1)
            if area > max_area:
                rect = Polygon([(tile.x, tile.y), (tile.x, other_tile.y), (other_tile.x, other_tile.y), (other_tile.x, tile.y)])
                if p.contains(rect):
                    max_area = area
    return max_area
