def part_1(parsed_input: tuple[list[tuple[int, int]], list[int]]) -> int:
    ranges, ids = parsed_input
    count = 0

    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break

    return count

def part_2(ranges: list[tuple[int, int]]) -> int:
    merged_ranges = []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    for current_start, current_end in sorted_ranges:
        if not merged_ranges or merged_ranges[-1][1] < current_start - 1:
            merged_ranges.append((current_start, current_end))
        else:
            last_start, last_end = merged_ranges[-1]
            merged_ranges[-1] = (last_start, max(last_end, current_end))

    total_covered = sum(end - start + 1 for start, end in merged_ranges)
    return total_covered