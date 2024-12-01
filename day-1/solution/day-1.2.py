with open('/Users/rtimganov/Repositories/aoc-2024/day-1/inputs/input_2.txt') as f:
    lines = f.readlines()
    res = 0
    first_sort = []
    second_sort = []
    for l in lines:
        print(l)
        first_sort.append(int(l.split()[0]))
        second_sort.append(int(l.split()[-1]))
    first_sort.sort()
    second_sort.sort()
    check_dict = {}

    for f in first_sort:
        res += f * second_sort.count(f)
    print(res)