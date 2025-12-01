def count_zero_passes(moves):    
    dial_position = 50
    zero_counter = 0

    for d, a in moves:
        old_position = dial_position

        if d == "L":
            dial_position -= a
        else:
            dial_position += a
        
        if d == "L":
            crossings = (old_position - dial_position) // 100
            if(old_position % 100 < dial_position % 100):
                crossings += 1
            zero_counter += crossings
        else:
            crossings = (dial_position - old_position) // 100
            if dial_position % 100 < old_position % 100:
                crossings += 1
            zero_counter += crossings
        dial_position %= 100
    
    return zero_counter