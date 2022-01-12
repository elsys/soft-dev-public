class Picture:
    def __init__(self, colums, lines, matrix):
        self.colums = colums
        self.lines = lines
        self.matrix = matrix

    def check_matrix(self):
        for i in range(0, self.colums):
            for y in range(0, self.lines):
                if self.matrix[i][y] < 0 or self.matrix[i][y] > 255:
                        return False
        return True

def check_element(matrix, x, y, colums, lines, sum, flag):
    if matrix[x][y] == 0:
        return [[0], [0], 0]

    random_point = matrix[x][y]
    sum[0] = sum[0] + matrix[x][y]
    flag[0] = flag[0] + 1
    matrix[x][y] = 0

    if x < (colums - 1):
        check_element(matrix, x + 1, y, colums, lines, sum, flag)
    
    if  x < (colums - 1) and y < (lines - 1):
        check_element(matrix, x + 1, y + 1, colums, lines, sum, flag)

    if y < (lines - 1):
        check_element(matrix, x, y + 1, colums, lines, sum, flag)[0]


    return [sum, flag, random_point]

def avg_brightness(picture):
    working_matrix = picture.matrix
    avgs = []
    avgs_index = 0
    

    for i in range(0, picture.colums):
        for y in range(0, picture.lines):
            sum = [0]
            flag = [0]
            result = [0, 0]
            result = check_element(working_matrix, i, y, picture.colums, picture.lines, sum, flag)
            sum = result[0]
            flag = result[1]

            if sum[0] > 0:
                print(f'Random point in area {avgs_index + 1} : {result[2]} \n')
                avgs.insert(avgs_index, sum[0] / flag[0])
                avgs_index = avgs_index + 1
   
    avgs.sort(reverse = True)

    return avgs

matrix = [[2, 2, 0, 5, 3],
          [0, 0, 0, 3, 5],
          [0, 0, 0, 0, 0],
          [0, 1, 2, 3, 0],
          [0, 0, 0, 0, 0]]

p1 = Picture(5, 5, matrix)

if p1.check_matrix() is False:
    print("Invalid matrix numbers!")
else:
    average_p1 = avg_brightness(p1)

    print("\nAverage brightness of areas:\n")

    print(average_p1)

    for i in range (0, len(average_p1)):
        print(f'\nArea {i + 1} :  {average_p1[i]}\n')