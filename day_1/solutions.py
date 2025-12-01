__all__ = ["count_zero_returns", "count_zero_passes"]

DIAL_MAX = 100
DIAL_START = 50

def count_zero_returns(moves: list[tuple[str, int]]) -> int:    
    dial_position = DIAL_START
    zero_counter = 0

    for d, a in moves:
        if d == "L":
            dial_position -= a
        else:
            dial_position += a
        
        dial_position %= DIAL_MAX

        if dial_position == 0:
            zero_counter += 1
    
    return zero_counter

def count_zero_passes(moves: list[tuple[str, int]]) -> int:
    dial_position = DIAL_START
    zero_counter = 0

    for d, a in moves:
        old_position = dial_position

        if d == "L":
            dial_position -= a
        else:
            dial_position += a
        
        if d == "L":
            crossings = (old_position - dial_position) // DIAL_MAX
            if(old_position % DIAL_MAX < dial_position % DIAL_MAX):
                crossings += 1
            zero_counter += crossings
        else:
            crossings = (dial_position - old_position) // DIAL_MAX
            if dial_position % DIAL_MAX < old_position % DIAL_MAX:
                crossings += 1
            zero_counter += crossings
        dial_position %= 100
    
    return zero_counter

