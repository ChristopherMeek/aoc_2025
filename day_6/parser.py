import re

def parse_1(input: str) -> list[tuple[str, list[int]]]:
    lines = input.strip().split("\n")
    operators = re.split(r"\s+", lines.pop())

    problems = []

    for i, operator in enumerate(operators):
        operands = []
        for line in lines:
            nums = re.split(r"\s+", line.strip())
            operands.append(int(nums[i]))
        problems.append((operator, operands))
    
    return problems

# THis could get ugly, but I have an idea
# parsing the operators line character by character will tell us the width of each column
# then we can use that to parse each line into its columns
# then parse the ints out by index
def parse_2(input: str): # -> list[tuple[str, list[int]]]:
    lines = input.splitlines()
    operator_line = lines.pop()
    operators = []
    widths = []
    
    current_width = 0
    current_operator = ""
    for char in operator_line:
        if char == "+" or char == "*":
            if current_operator != "":
                operators.append(current_operator)
                widths.append(current_width)
            current_operator = char
            current_width = 0
        else:
            current_width += 1
    
    operators.append(current_operator)
    widths.append(current_width+1)


    results = []
    for i, operand in enumerate(operators):
        col_width = widths[i]
        cols = []
        for line in lines:
            start_index = sum(widths[:i]) + i
            end_index = start_index + col_width
            col_str = line[start_index:end_index]
            cols.append(col_str)
        operands = []
        for i in range(col_width):
            num_str = "".join(col[i] for col in cols).strip()
            operands.append(int(num_str))
    
        results.append((operand, operands))

    return results