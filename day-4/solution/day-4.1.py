with open('/Users/rtimganov/Repositories/aoc-2024/day-4/inputs/input_1.txt') as f:
    lines = f.readlines()
    matrix = []
    total_res = 0
    res = []
    target_words = [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]
    
    for l in lines:
        mini_line = []
        l = l.strip()
        for ch in l:
            mini_line.append(ch)
        matrix.append(mini_line)

    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 3):
            temp = [matrix[i][j], matrix[i][j+1], matrix[i][j+2], matrix[i][j+3]]
            if temp in target_words:
                total_res += 1

    for i in range(len(matrix) - 3):
        for j in range(len(matrix[i])):
            temp = [matrix[i][j], matrix[i+1][j], matrix[i+2][j], matrix[i+3][j]]
            if temp in target_words:
                total_res += 1

    for i in range(len(matrix) - 3):
        for j in range(len(matrix[i]) - 3):
            temp = [matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3]]
            if temp in target_words:
                total_res += 1

    for i in range(len(matrix) - 3):
        for j in range(3, len(matrix[i])):
            temp = [matrix[i][j], matrix[i+1][j-1], matrix[i+2][j-2], matrix[i+3][j-3]]
            if temp in target_words:
                total_res += 1

    print(total_res)
