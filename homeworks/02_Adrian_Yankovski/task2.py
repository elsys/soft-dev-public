def num_ways(n):
 

    if n < 0:
        return 0
 
    
    if n == 0:
        return 1
 
   
    return num_ways(n - 1) + num_ways(n - 2) 
 
 

 if __name__ == '__main__':

    n = 2
    
if n > 1:
    print('ways to reach stair {n} are', num_ways(n))
    
