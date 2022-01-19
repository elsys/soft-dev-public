matrix = [
    [1,   2, 3,   4,   5,  6],
    [0,   0, 0,   0,   0,  0],
    [2, 0, 14, 180, 0,  205],
    [0,   0, 85,  0,   184, 0],
    [108, 0, 0,   0,   0,  255],
    [68,  0, 174, 0,   17, 0]
]

def blow(matrix, _i, _j):
    avg = []
    for i in range(_i - 1, _i + 2):
        for j in range(_j - 1, _j + 2):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]):
                continue
            if matrix[i][j] != 0:
                avg.append(matrix[i][j])
                matrix[i][j] = 0
                avg.extend(blow(matrix, i, j))
    return avg

def avg_brightness(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                avg    = blow(matrix, i, j)
                result = sum(avg) / len(avg)
                print(f"({i}:{j}) = {result:.2f}")

avg_brightness(matrix)
