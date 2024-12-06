import re
from itertools import combinations

rules_list = []
seq_list = []
res = 0
with open('/Users/rtimganov/Repositories/aoc-2024/day-5/inputs/input_1.txt') as f:
    lines = f.read()
    rules = re.findall(r'\d+\|\d+', lines)
    rules_list = [tuple(map(int,r.split('|'))) for r in rules]
with open('/Users/rtimganov/Repositories/aoc-2024/day-5/inputs/input_1.1.txt') as f:
    lines = f.readlines()
    seq_list = [list(map(int, l.strip().split(','))) for l in lines]
#print(rules_list)
# print(seq_list)
good_seqs = []
for seq in seq_list:
    is_good_seq = True
    pairs = list(combinations(seq, 2))
    for p in pairs:
        if p in rules_list:
            continue
        else:
            is_good_seq = False
    if is_good_seq:
        good_seqs.append(seq)
for gs in good_seqs:
    res += gs[len(gs)//2]
print(res)