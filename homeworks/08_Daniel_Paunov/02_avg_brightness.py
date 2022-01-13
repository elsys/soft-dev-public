
#rows = 20
#columns = 30

#matrix = [ [0] * columns for i in range(rows) ]

matrix = [
    [3, 0, 0, 3, 139, 119, 3, 19, 63, 3, 0, 0, 3, 179, 163, 3, 7, 67, 3, 0],
    [59, 0, 0, 0, 71, 47, 0, 15, 115, 135, 0, 0, 0, 39, 87, 27, 51, 99, 51, 0],
    [0, 0, 0, 0, 0, 0, 43, 35, 63, 135, 115, 0, 0, 0, 0, 0, 35, 95, 99 ,107],
    [3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 135, 119, 3, 0, 0, 3, 51, 19, 3, 91],
    [147, 115, 79, 27, 0, 0, 0, 0, 0, 0, 27, 139, 167, 139, 119, 139, 103, 0, 0, 0],
    [139, 171, 75, 0, 0, 0, 0, 0, 19, 0, 0, 0, 151, 255, 243, 123, 63, 7, 0, 0],
    [3, 123, 99, 3, 0, 0, 3, 171, 183, 3, 0, 0, 3, 187, 191, 3, 0, 47, 3, 0],
    [0, 63, 103, 55, 0, 0, 11, 179, 227, 83, 0, 0, 0, 39, 19, 0, 0, 63, 67, 0],
    [7, 0, 15, 0, 0, 0, 0, 99, 191, 107, 23, 19, 0, 0, 0, 0, 11, 67, 99, 139],
    [3, 0, 0, 3, 0, 0, 3, 95, 111, 3, 0, 59, 3, 0, 0, 3, 63, 7, 3, 159],
    [15, 0, 0, 39, 0, 0, 35, 51, 0, 0, 0, 0, 0, 0, 0, 43, 55, 0, 0, 95],
    [63, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 91, 123, 31, 0, 27, 31, 59],
    [3, 0, 0, 3, 71, 35, 3, 0, 0, 3, 35, 0, 3, 215, 215, 3, 0, 0, 3, 0],
    [0, 0, 0, 99, 223, 235, 179, 39, 0, 0, 39, 47, 91, 247, 227, 23, 0, 0, 0, 0],
    [0, 0, 0, 75, 255, 255, 167, 0, 0, 0, 51, 123, 127, 203, 191, 35, 0, 0, 0, 63],
    [3, 0, 0, 3, 195, 187, 3, 0, 0, 3, 95, 83, 3, 59, 103, 3, 0, 0, 3, 207],
    [67, 0, 0, 35, 147, 43, 0, 0, 0, 111, 123, 0, 0, 0, 83, 51, 0, 0, 7, 183],
    [51, 39, 0, 59, 87, 0, 0, 0, 0, 87, 87, 0, 0, 0, 99, 99, 0, 0, 15, 107],
    [3, 51, 0, 3, 39, 0, 3, 15, 0, 3, 51, 0, 3, 91, 55, 3, 0, 0, 3, 39],
    [0, 0, 0, 0, 19, 95, 155, 111, 0, 0, 0, 0, 79, 123, 0, 0, 0, 0, 11, 0]
]

rows = len(matrix)
columns = len(matrix[0])

def print_matrix(matrix):
    print_matrix = ""
    for x in matrix:
        for y in x:
            print_matrix += str(y)
            print_matrix += "\t"
            
        if columns > 20:
            print_matrix += "/"
            
        print_matrix += "\n"

    print(print_matrix.expandtabs(4))

def avg_brightness(matrix):
    avg_bright = {}
    def total_brightness(x, y):
        if not (0 <= x < rows and 0 <= y < columns) or matrix[x][y] <= 0:
            return (0, 0)

        count = 1
        brightness = matrix[x][y]
        matrix[x][y] *= -1

        temp = []

        temp.append(total_brightness(x, y-1))
        temp.append(total_brightness(x+1, y-1))
        temp.append(total_brightness(x+1, y))
        temp.append(total_brightness(x+1, y+1))
        temp.append(total_brightness(x, y+1))
        temp.append(total_brightness(x-1, y+1))
        temp.append(total_brightness(x-1, y))
        temp.append(total_brightness(x-1, y-1))

        for x in temp:
            brightness += x[0]
            count += x[1]
        
        return (brightness, count)

    for x in range(rows):
        for y in range(columns):
            if matrix[x][y] > 0:
                temp = total_brightness(x, y)
                avg_bright[(y, x)] = temp[0] / temp[1]
            matrix[x][y] *= -1

    sorted_bright = dict(sorted(avg_bright.items(), key = lambda x: x[1], reverse = True))

    return sorted_bright

avg_bright = avg_brightness(matrix)

for x in avg_bright:
    print(str(x) + " : " + str(round(avg_bright[x] * 100000) / 100000))
