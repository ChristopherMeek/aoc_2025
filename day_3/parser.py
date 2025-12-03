from parsy import string, regex, seq

_batteries = regex(r"\d+")

banks_parser = _batteries.sep_by(string("\n"))