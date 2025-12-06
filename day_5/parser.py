def parse(input : str) -> tuple[list[tuple[int, int]], list[int]]:
    lines = input.splitlines()

    ranges_finished = False
    ranges = []
    ids = []
    for line in lines:
        if line == "":
            ranges_finished = True
            continue

        if not ranges_finished:
            parts = line.split("-")
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))
        else:
            ids.append(int(line))

    return ranges, ids