def part_1(map: dict[tuple[int, int], str]) -> int:
    accessible_rolls = 0
    for coord, value in map.items():
        if(value == "@"):
            if(rolls_adjacent(coord, map) < 4):
                accessible_rolls += 1

    return accessible_rolls

def part_2(map: dict[tuple[int, int], str]) -> int:
    accessible_roll_count = 0
    accessible_rolls = []

    for coord, value in map.items():
        if(value == "@"):
            if(rolls_adjacent(coord, map) < 4):
                accessible_rolls.append(coord)
                accessible_roll_count += 1

    if(accessible_roll_count == 0):
        return 0
    
    for coord in accessible_rolls:
        x, y = coord
        map[(x, y)] = "."

    return accessible_roll_count + part_2(map)


def rolls_adjacent(coord: tuple[int, int], map: dict[tuple[int, int], str]) -> int:    
    x, y = coord
    count = 0
        
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            adjacent_coord = (x + dx, y + dy)
            if adjacent_coord in map and map[adjacent_coord] == '@':
                count += 1
    
    return count