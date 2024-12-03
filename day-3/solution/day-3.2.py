import re

pattern = "(mul\([0-9]{1,3},[0-9]{1,3}\))|(don\'t\(\))|(do)"

def mul(a, b):
    return a*b

with open('/Users/rtimganov/Repositories/aoc-2024/day-3/inputs/input_2.txt') as f:
    lines = f.read()
    res = 0
    muls = re.findall(pattern, lines)
    print(muls)
    is_good = True
    for m in muls:
        if is_good and m[0]:
            f, s = list(map(int, re.findall(r'\d+', m[0])))
            res += f * s
        elif is_good and m[1]:
            is_good = False
        elif not is_good and m[-1]:
            is_good = True

