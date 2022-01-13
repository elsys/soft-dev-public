
def get_neighbours(index, matrix):
    offsets = [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]

    neighbours = []
    neighbour = []
    for offset in offsets:
        neighbour = [x + y for x, y in zip(offset, index)]
        if (neighbour[0] >= 0 and neighbour[0] < len(matrix)) and (neighbour[1] >= 0 and neighbour[1] < len(matrix[neighbour[0]])):
            if matrix[neighbour[0]][neighbour[1]] != 0:
                neighbours.append(neighbour)
    return neighbours #returns index


def calculate_sum(matrix, index, has_accessed=[]):
    brightness = matrix[index[0]][index[1]]
    has_accessed.append(index)

    neighbours = get_neighbours(index, matrix)
    neighbours = [neighbour for neighbour in neighbours if neighbour not in has_accessed]

    # print(index, ':', neighbours)

    if(len(neighbours) == 0):
        return brightness

    for neighbour in neighbours:
        if neighbour not in has_accessed:
            brightness += calculate_sum(matrix, neighbour, has_accessed)
    return brightness





def avg_brightness(matrix):
    has_accessed = []
    sum = 0
    old_len = 0
    cells = 0

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if matrix[i][j] == 0 or [i,j] in has_accessed:
                continue
            # neighbours = get_neighbours([i,j], matrix)
            sum = calculate_sum(matrix, [i,j], has_accessed)
            cells = len(has_accessed) - old_len

            print("Sum:", sum)
            print("Cells:", cells)
            print("Average brightness:", sum/cells, "\n")
            old_len += cells



matrix = [
        [85,  0, 0, 108],
        [0,  0, 127, 0],  
        [0,  0, 0, 0],
        [0,  0, 0, 0],  
        [0,  0, 7, 0],
        [0,  0, 0, 0],
        [0,  9, 0, 0],
        [0,  0, 0, 0]
    ]
avg_brightness(matrix)