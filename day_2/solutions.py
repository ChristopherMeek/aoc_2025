__all__ = ["part_1", "part_2"]

def part_1(parsed_input):
    """Find IDs where the first half of digits equals the second half and return their sum."""
    repeating_ids = []

    for start, end in parsed_input:
        id_range = list(range(start, end + 1))

        for id in id_range:
            str_id = str(id)
            if len(str_id) % 2 == 0 and has_repeat_of_length(str_id, len(str_id) // 2):
                repeating_ids.append(id)
    
    return sum(repeating_ids)

def part_2(parsed_input):
    repeating_ids = []

    for start, end in parsed_input:
        id_range = list(range(start, end + 1))

        for id in id_range:
            str_id = str(id)
            if(len(str_id) == 1): 
                continue
            
            for length in range(1, len(str_id)//2 + 1):
                if len(str_id) % length == 0 and has_repeat_of_length(str_id, length):
                    #print(f"Found repeating ID: {id} with segment length {length}")
                    repeating_ids.append(id)
    
    return sum(set(repeating_ids))
    

def has_repeat_of_length(s: str, length: int) -> bool:
    if len(s) % length != 0:
        return False
    
    # Comprehension: create segments s[i,i+length] all the way to the end of s, skipping length as we go
    # eg. "abcdefgh" -> "ab", "cd", "ef", "gh" for length=2
    segments = [s[i:i+length] for i in range(0, len(s), length)]

    return len(set(segments)) == 1