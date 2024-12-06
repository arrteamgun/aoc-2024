import re
from itertools import combinations


rules_list = []
seq_list = []
res = 0
with open('/Users/rtimganov/Repositories/aoc-2024/day-5/inputs/input_2.txt') as f:
    lines = f.read()
    rules = re.findall(r'\d+\|\d+', lines)
    rules_list = [tuple(map(int, r.split('|'))) for r in rules]
with open('/day-5/inputs/input_2.1.txt') as f:
    lines = f.readlines()
    seq_list = [list(map(int, l.strip().split(','))) for l in lines]

good_seqs = []
for seq in seq_list:
    is_good_seq = True
    pairs = list(combinations(seq, 2))
    for p in pairs:
        if p in rules_list:
            continue
        else:
            is_good_seq = False
    if not is_good_seq:
        good_seqs.append(seq)

for gseq in good_seqs:
    for i in range(len(gseq) - 1):
        for lef_r, rig_r in rules_list:
            try:
                _l, _r = gseq.index(lef_r), gseq.index(rig_r)
                if _l > _r:
                    gseq[_l],gseq[_r] = gseq[_r],gseq[_l]
            except:
                pass

print(good_seqs)

for gs in good_seqs:
    res += gs[len(gs)//2]
print(res)
