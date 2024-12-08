import os
import sys
sys.setrecursionlimit(10**6)
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../inputs/input_2.txt")
obst = 0 #obstacles that create loops
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(path, 'r') as f:
    lines = f.readlines()
    matrix = [[ch for ch in l.strip()] for l in lines]
    mark_i, mark_j = 0, 0
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == '^':
                mark_i, mark_j = i, j
    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != '.':
                continue
            matrix[x][y] = '#'
            mi, mj = mark_i, mark_j
            visited = set()
            cd = 0
            while True:
                if (cd, mi, mj) in visited:
                    obst += 1
                    break
                visited.add((cd, mi, mj))
                next_i = mi + direction[cd][0]
                next_j = mj + direction[cd][1]
                if not (0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0])): #out of bounds
                    break
                if matrix[next_i][next_j] == '#' or (next_i == x and next_j == y): #transform if bounds or #
                    cd = (cd + 1) % 4
                else:
                    mi, mj = next_i, next_j
            # for m in matrix:
            #     print(*m, sep='')
            # print('-'*50)
            matrix[x][y] = '.'
print('obst:', obst)
