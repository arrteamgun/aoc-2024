with open('/Users/rtimganov/Repositories/aoc-2024/day-4/inputs/input_2.txt') as f:
    lines = f.readlines()
    matrix = []
    total_res = 0

    for l in lines:
        mini_line = []
        l = l.strip()
        for ch in l:
            mini_line.append(ch)
        matrix.append(mini_line)
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if matrix[i][j] == 'A':
                if ''.join([matrix[i-1][j-1], matrix[i][j], matrix[i+1][j+1]]) in ['MAS', 'SAM']:
                    if ''.join([matrix[i+1][j-1], matrix[i][j], matrix[i-1][j+1]]) in ['MAS', 'SAM']:
                        total_res += 1
    print(total_res)
