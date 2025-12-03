def part_1(parsed_input: list[tuple[int, int]]) -> int:    
    repeating_ids = []

    for start, end in parsed_input:
        for num in range(start, end + 1):
            str_num = str(num)
            # Only even-length numbers can have equal halves
            if len(str_num) % 2 == 0 and _has_repeat_of_length(str_num, len(str_num) // 2):
                repeating_ids.append(num)
    
    return sum(repeating_ids)

def part_2(parsed_input: list[tuple[int, int]]) -> int:    
    repeating_ids = []

    for start, end in parsed_input:
        for num in range(start, end + 1):
            str_num = str(num)
            # Single-digit numbers don't have repeating segments
            if len(str_num) == 1:
                continue
            
            # Check all possible segment lengths from 1 to half the string length
            for length in range(1, len(str_num) // 2 + 1):
                if _has_repeat_of_length(str_num, length):
                    repeating_ids.append(num)
                    break  # Found a repeating pattern, no need to check other lengths
    
    return sum(set(repeating_ids))

def _has_repeat_of_length(s: str, length: int) -> bool:        
    if len(s) % length != 0:
        return False
        
    segments = [s[i:i+length] for i in range(0, len(s), length)]

    return len(set(segments)) == 1