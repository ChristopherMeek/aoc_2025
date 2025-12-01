def count_zero_returns(moves):    
    dial_position = 50
    zero_counter = 0

    for d, a in moves:
        if d == "L":
            dial_position -= a
        else:
            dial_position += a
        
        dial_position %= 100

        if dial_position == 0:
            zero_counter += 1
    
    return zero_counter
