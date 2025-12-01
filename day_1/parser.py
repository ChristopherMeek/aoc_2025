from parsy import string, regex, seq

__all__ = ["moves_parser"]

direction = string("L") | string("R")
amount = regex(r"\d+").map(int)
move = seq(direction, amount).combine(lambda d, a: (d, a))

moves_parser = move.sep_by(string("\n"))