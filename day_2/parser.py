from parsy import string, regex, seq

__all__ = ["ranges_parser"]

number = regex(r"\d+").map(int)
hyphen = string("-")
range_pair = seq(number, hyphen, number).combine(lambda start, _, end: (start, end))

ranges_parser = range_pair.sep_by(string(","))