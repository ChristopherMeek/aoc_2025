from math import prod

def part_1(problems: list[tuple[str, list[int]]]) -> int:
    result = 0

    for operator, operands in problems:
        if operator == '+':
            result += sum(operands)
        elif operator == '*':
            result += prod(operands)
    
    return result
        