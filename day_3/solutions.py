def solve(banks: list[str], digits: int) -> int:
    total = 0
    for bank in banks:        
        max_value = max_joltage([int(d) for d in bank], digits)
        total += max_value        
    return total
    

def max_joltage(bank: list[int], digits: int) -> int:
    if digits == 1:
        return max(bank)
        
    max_digit = max(bank[:-(digits - 1)])
    idx = bank.index(max_digit)
    return max_digit * (10 ** (digits - 1)) + max_joltage(bank[idx + 1 :], digits - 1)