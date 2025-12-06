import requests

def get_aoc_data(day: int) -> str:
    cookies = dict(session="53616c7465645f5f15a26ce24be9a9a852d2a6e80e38e76fa94586829dbbee68434e077ad27c1ff6edc7a6215a373ed39bbf8a9e93d79d285b1f759f0316e0fc")
    response = requests.get(f"https://adventofcode.com/2025/day/{day}/input", cookies=cookies)
    return response.text
