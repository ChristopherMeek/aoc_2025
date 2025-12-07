from .grid import Grid, Coordinate

def part_1(manifold: Grid) -> int:
    start = manifold.find('S')

    number_of_splits = 0
    beam_ends = {start.x}

    for y in range(manifold.height):
        new_beam_ends = beam_ends.copy()
        for x in beam_ends:
            if(manifold.at(Coordinate(x, y)) == '.'):
                manifold.set_at(Coordinate(x, y), '|')                
            elif(manifold.at(Coordinate(x,y)) == '^'):
                number_of_splits += 1
                new_beam_ends.remove(x)
                new_beam_ends.add(x-1)
                new_beam_ends.add(x+1)              
        
        beam_ends = new_beam_ends

    return number_of_splits

def part_2(manifold: Grid) -> int:
    start = manifold.find('S')
    
    beam_ends = {
        start.x: 1
    }

    for y in range(manifold.height):        
        new_beam_ends = beam_ends.copy()
                
        for x, count in beam_ends.items():
            if(manifold.at(Coordinate(x, y)) == '.'):
                manifold.set_at(Coordinate(x, y), '|')                
            elif(manifold.at(Coordinate(x,y)) == '^'):
                del new_beam_ends[x]                
                new_beam_ends[x-1] = new_beam_ends.get(x-1, 0) + count
                new_beam_ends[x+1] = new_beam_ends.get(x+1, 0) + count
                
        beam_ends = new_beam_ends

    return sum(beam_ends.values())