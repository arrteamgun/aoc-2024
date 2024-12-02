def validate_levels(level: list):
    if level == sorted(level) or level == sorted(level, reverse=True):
        dif = [abs(j - i) for i, j in zip(level[:-1], level[1:])]
        return all(0 < d <= 3 for d in dif)
    return False

with open('/Users/rtimganov/Repositories/aoc-2024/day-2/inputs/input_2.txt') as f:
    lines = f.readlines()
    res = 0
    for l in lines:
        level = list(map(int, l.split()))
        if validate_levels(level):
            res += 1
        else:
            for i in range(len(level)):
                level_copy = level[:i] + level[i+1:]
                if validate_levels(level_copy):
                    res += 1
                    break
    print(res)
