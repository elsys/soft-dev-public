#walk trough every element and his neighbours
# if it has a positive value -> add to sum
# if not -> skip
#if the whole region is blocked -> search for a new region

def walk_trough(matrix, m, n):

    if m not in range(len(matrix)) or n not in range(len(matrix)):
        return 0, 0
    if matrix[m][n] == 0:
        return 0, 0

    sum = matrix[m][n]
    pixels = 1
    matrix[m][n] = 0

    #bottom neighbour
    if(m+1 in range(0, 5) and matrix[m+1][n] > 0): 
            new_sum, new_pixels = walk_trough(matrix, m+1, n)
            sum += new_sum
            pixels += new_pixels
    
    #bottom left neighbour
    elif(m+1 in range(0, len(matrix)) and  n+1 in range(0, len(matrix)) and matrix[m+1][n+1] > 0):
            new_sum, new_pixels = walk_trough(matrix, m+1, n+1)
            sum += new_sum
            pixels += new_pixels

    #bottom right neighbour      
    elif( m+1 in range(0, len(matrix)) and  n-1 in range(0, len(matrix)) and matrix[m+1][n-1] > 0 ):
            new_sum, new_pixels = walk_trough(matrix, m+1, n-1)
            sum += new_sum
            pixels += new_pixels

    #top right neigbour    
    elif(n+1 in range(0, len(matrix)) and  m-1 in range(0, len(matrix)) and matrix[m-1][n+1] > 0 ):
            new_sum, new_pixels = walk_trough(matrix, m+1, n+1)
            sum += new_sum
            pixels += new_pixels
    
    #top left neighbour
    elif(m-1 in range(0, len(matrix)) and  n-1 in range(0, len(matrix)) and matrix[m-1][n-1] > 0 ):
        new_sum, new_pixels = walk_trough(matrix, m-1, n-1)
        sum += new_sum
        pixels += new_pixels

    #top neighbour
    elif( m-1 in range(0, len(matrix)) and matrix[m-1][n] > 0 ):
        new_sum, new_pixels = walk_trough(matrix, m-1, n)
        sum += new_sum
        pixels += new_pixels

    #right neigbour
    elif(n-1 in range(0, len(matrix)) and matrix[m][n-1] > 0 ):
        new_sum, new_pixels = walk_trough(matrix, m, n-1)
        sum += new_sum
        pixels += new_pixels

    #left neighbour
    elif( n+1 in range(0, len(matrix)) and matrix[m][n+1] > 0 ):
            new_sum, new_pixels = walk_trough(matrix, m, n+1)
            sum += new_sum
            pixels += new_pixels

    return sum, pixels
    
def avg_brightness(matrix):
    r_index = 0
    c_index = 0
    for i in matrix:
        for j in i:
            if matrix[r_index][c_index] == 0:
                continue

            pixels, sum = walk_trough(matrix, r_index, c_index)
            print(f"({r_index}, {c_index}) {sum/pixels}")
            c_index += 1
        
        r_index += 1


m = [
        [170, 0, 0, 255, 221, 0],
        [68, 0, 17, 0, 0, 68],
        [221, 0, 238, 136, 0, 255],
        [0, 0, 85, 0, 136, 238],
        [238, 17, 0, 68, 0, 255],
        [85, 170, 0, 221, 17, 0]
    ]
avg_brightness(m)


