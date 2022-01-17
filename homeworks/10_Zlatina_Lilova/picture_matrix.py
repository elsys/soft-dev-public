#walk trough every element and his neighbours
# if it has a positive value -> add to sum
# if not -> skip
#if the whole region is blocked -> search for a new region

#avg = []

def walk_trough(matrix, m, n):
    
    avg = []

    if m not in range(len(matrix)) or n not in range(len(matrix)):
        return avg
    if matrix[m][n] == 0:
        return avg
    #print("Element: ", matrix[m][n], m, n)
    avg.append(matrix[m][n])
    matrix[m][n] = 0

    
    for i in range(m-1, m+2):
        for j in range(n-2, n+2):
            if i in range(len(matrix)) and j in range(len(matrix[0])):
            
                if i == m and j == n:
                    continue
            
                if matrix[i][j] != 0:
                    avg.extend(walk_trough(matrix, i, j))

    

    return avg 
    


def avg_brightness(mm):
    r_index = 0
    c_index = 0
    matrix = mm.copy()
    for r_index, row in enumerate(matrix):
        for c_index, element in enumerate(row):
            if element == 0:
                continue
            #print(matrix)
            sum = walk_trough(matrix, r_index, c_index)
            average = 0
           # print(avg)
            for each in sum:
                average += each
            print(f"({r_index}, {c_index}) {(average/len(sum)):.2f}")
            #avg.clear();


m = [
        [170, 0, 0, 255, 221, 0],
        [68, 0, 17, 0, 0, 68],
        [221, 0, 238, 136, 0, 255],
        [0, 0, 85, 0, 136, 238],
        [238, 17, 0, 68, 0, 255],
        [85, 170, 0, 221, 17, 0]
    ]
avg_brightness(m)


