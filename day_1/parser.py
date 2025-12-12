from parsy import string, regex, seq

direction = string("L") | string("R")
amount = regex(r"\d+").map(int)
move = seq(direction, amount).combine(lambda d, a: (d, a))

moves_parser = move.sep_by(string("\n"))