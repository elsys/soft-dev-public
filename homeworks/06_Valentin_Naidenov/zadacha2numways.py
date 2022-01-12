def printCountDP(dist):
    count = [0] * (dist + 1)
    
    count[0] = 1
    if dist >= 1 :
        count[1] = 1
    if dist >= 2 :
        count[2] = 2
    
    
    for i in range(2, dist + 1):
        count[i] = (count[i-1] + 
                   count[i-2])
        
    return count[dist];


dist = 4;
print( printCountDP(dist))

