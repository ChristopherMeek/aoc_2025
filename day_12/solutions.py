def sanity_check(data: tuple[list[int], list[tuple[tuple[int,int], list[int]]]]) -> int:
    preset_sizes, trees = data

    total_that_could_fit = 0
    for tree in trees:
        dimensions, present_counts = tree
        
        size = dimensions[0] * dimensions[1]
        required_space = sum([num_presents * preset_sizes[i] for i,num_presents in enumerate(present_counts)])

        if required_space <= size:
            total_that_could_fit += 1

        print(f"Tree size: {size}, Required space: {required_space}, Could fit: {required_space <= size}, Space left: {size - required_space}")
    return total_that_could_fit