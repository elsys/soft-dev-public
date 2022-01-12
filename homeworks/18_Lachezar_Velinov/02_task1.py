

def getSectorValues(matrix, rowpos, columnpos, sectorList): #finds all the values of a sector and returns them
    sectorList.append(matrix[rowpos][columnpos]) 
    matrix[rowpos][columnpos] = 0 #turns an appended square into a black square
    for i in range(-1, 2):
        for j in range(-1, 2):
            if rowpos + i >= 0 and columnpos + j >= 0 and rowpos + i < len(matrix) and columnpos + j < len(matrix[i]): #check if location is in range of the matrix
                if matrix[rowpos+i][columnpos+j] != 0: #check if square is non black
                    getSectorValues(matrix, rowpos+i, columnpos+j, sectorList) #reccursive calling
    return


def findSector(matrix): #looks for a sector and returns it's average value
    returnValueList = [] #holds average value of every sector
    sectorList = [] #holds all the values of a single sector
    for rowpos, row in enumerate(matrix): 
        for columnpos, column in enumerate(row): #go throught the matrix to find a non black square
            if matrix[rowpos][columnpos] > 0:
                getSectorValues(matrix, rowpos, columnpos, sectorList)
                average = 0 #average value of a sector
                for amount in sectorList:
                    average+=amount
                average /= len(sectorList)
                del sectorList[:] #reset the sector list
                returnValueList.append(average) #add average sector value to rest list

    return returnValueList


def avg_brightnes(matrix):    
    outputList = [] 
    outPutList = findSector(matrixCopy)
    outPutList.sort(reverse=True) #sort list in descending order
    for i in outPutList: #prints final values
        print (i)




matrix = ( #test matrix
    (170,   0,   0, 255, 221,   0),
    ( 68,   0,  17,   0,   0,  68),
    (221,   0, 238, 136,   0, 255),
    (  0,   0,  85,   0, 136, 238),
    (238,  17,   0,  68,   0, 255),
    ( 85, 170,   0, 221,  17,   0)
)

matrixCopy = [list(matrix_inner) for matrix_inner in matrix] #since we cannot use the original matrix, we make a copy
avg_brightnes(matrixCopy)
