from parsy import string, regex, seq

width = regex(r"\d+").map(int)
length = regex(r"\d+").map(int)
size = seq(width, string("x"), length).combine(lambda w, _, l: (w, l))

colon = string(":")
space = string(" ")
present_count = regex(r"\d+").map(int)

tree_parser = seq(
        size, colon, space, present_count, space, present_count, space, present_count, space, present_count, space, present_count, space, present_count
    ).combine(lambda size,_,__,pc1,___,pc2,____,pc3,_____,pc4,______,pc5,_______,pc6: (size, [pc1, pc2, pc3, pc4, pc5, pc6]))

tree_parser = tree_parser.sep_by(string("\n"))

def parse(input: str):
    segments = input.split('\n\n')

    tree_string = segments.pop().strip()
    trees = tree_parser.parse(tree_string)

    preset_sizes = []
    for present_string in segments:
        preset_sizes.append(present_string.count('#'))

    return (preset_sizes, trees)