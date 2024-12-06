import re
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../inputs/input_1.txt")

with open(path, 'r') as f:
    lines = f.readlines()
    direction = {
        '^': (0, (-1, 0)),
        '>': (1, (0, 1)),
        'V': (2, (1, 0)),
        '<': (3, (0, -1)),
    }

    matrix = []
    for l in lines:
        mini_line = []
        l = l.strip()
        for ch in l:
            mini_line.append(ch)
        matrix.append(mini_line)
    mark_i, mark_j = 0, 0
    total = 0
    for i in range(len(matrix) - 1):
        try:
            mark_i = i
            mark_j = matrix[i].index('^')
            break
        except:
            pass
    try:
        while True:
            current = matrix[mark_i][mark_j]
            go_next = matrix[mark_i+direction[current]
                             [-1][0]][mark_j+direction[current][-1][1]]
            if go_next != "#":
                go_next = current
                matrix[mark_i][mark_j] = 'X'
                mark_i, mark_j = mark_i + \
                    direction[current][-1][0], mark_j+direction[current][-1][1]
                matrix[mark_i][mark_j] = current
            else:
                if direction[current][0]+1 != 4:
                    value = [i for i in direction
                             if direction[i][0] == direction[current][0]+1][0]
                    matrix[mark_i][mark_j] = value

                else:
                    matrix[mark_i][mark_j] = '^'
    except IndexError:
        for m in matrix:
            for el in m:
                if el == 'X':
                    total += 1
        print(total+1)
