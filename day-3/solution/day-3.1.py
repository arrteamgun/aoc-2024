import re

pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)"

def mul(a, b):
    return a*b

with open('/Users/rtimganov/Repositories/aoc-2024/day-3/inputs/input_1.txt') as f:
    lines = f.read()
    res = 0
    muls = re.findall(pattern, lines)
    for m in muls:
        f, s = list(map(int, re.findall(r'\d+', m)))
        res += f*s

    print(res)
