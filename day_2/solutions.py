__all__ = ["part_1", "part_2"]

def part_1(parsed_input: list[tuple[int, int]]) -> int:
    """Find numbers where first half of digits equals second half.
    
    Args:
        parsed_input: List of (start, end) range tuples
    
    Returns:
        Sum of all numbers with repeating halves
    """
    repeating_ids = []

    for start, end in parsed_input:
        for num in range(start, end + 1):
            str_num = str(num)
            # Only even-length numbers can have equal halves
            if len(str_num) % 2 == 0 and has_repeat_of_length(str_num, len(str_num) // 2):
                repeating_ids.append(num)
    
    return sum(repeating_ids)

def part_2(parsed_input: list[tuple[int, int]]) -> int:
    """Find numbers that consist of repeated segments of any length.
    
    Args:
        parsed_input: List of (start, end) range tuples
    
    Returns:
        Sum of unique numbers with any repeating pattern
    """
    repeating_ids = []

    for start, end in parsed_input:
        for num in range(start, end + 1):
            str_num = str(num)
            # Single-digit numbers don't have repeating segments
            if len(str_num) == 1:
                continue
            
            # Check all possible segment lengths from 1 to half the string length
            for length in range(1, len(str_num) // 2 + 1):
                if has_repeat_of_length(str_num, length):
                    repeating_ids.append(num)
                    break  # Found a repeating pattern, no need to check other lengths
    
    return sum(set(repeating_ids))

def has_repeat_of_length(s: str, length: int) -> bool:
    """Check if string consists of repeated segments of given length.
    
    Args:
        s: String to check
        length: Length of each segment
    
    Returns:
        True if all segments are identical, False otherwise
    
    Example:
        has_repeat_of_length("abcabc", 3) -> True
        has_repeat_of_length("abcdef", 3) -> False
    """
    if len(s) % length != 0:
        return False
    
    # Create segments: split string into chunks of given length
    # e.g., "abcdefgh" with length=2 -> ["ab", "cd", "ef", "gh"]
    segments = [s[i:i+length] for i in range(0, len(s), length)]

    # If all segments are identical, set will have only 1 unique element
    return len(set(segments)) == 1