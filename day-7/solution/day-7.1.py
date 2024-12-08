import os
from itertools import permutations, product

#res = 0
totals = 0

def get_permutations(numbs: list):
    return product('*+|', repeat=len(numbs)-1)

def get_res(to_eval: list):
    try:
        eq = ''.join(map(str,to_eval))
        eq = eq.replace('|', '')
        res = eval(eq)
        return res
    except:
        print('wrong list', to_eval)

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../inputs/input_1.txt")
with open(path, 'r') as f:
    lines = f.readlines()
    d = [(int(l.split(':')[0]), list(map(int, (l.split(':')[1].strip().split())))) for l in lines]
    for row in d:
        symb_list = list(get_permutations(row[-1]))
        eq = False
        for sl in symb_list:
            res = [None]*(len(row[-1])+len(sl))
            res[::2] = row[-1]
            res[1::2] = sl
            while res:
                to_eval = get_res(res[0:3])
                new_res = res[3:]
                if not new_res:
                    if to_eval == row[0]:
                        eq = True
                    break
                res = [to_eval, *new_res]
        if eq:
            totals += row[0]
print(totals)
                
                
                
            
