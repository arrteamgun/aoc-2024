with open('/Users/rtimganov/Repositories/aoc-2024/day-2/inputs/input_1.txt') as f:
    lines = f.readlines()
    res = 0
    for l in lines:
        posl = list(map(int, l.split()))
        if posl == sorted(posl) or posl == sorted(posl, reverse=True):
            dif = list(map(abs, ([j-i for i, j in zip(posl[:-1], posl[1:])])))
            changed = list(filter(lambda x: x > 3 or x == 0, dif))
            if not changed:
                res += 1
    print(res)
            
