
ways = 0

def num_ways(steps):
    
    if steps == 0:
        global ways
        ways = ways +1
        return 
    
    num_ways(steps - 1)
    if steps > 1:
        num_ways(steps - 2)
    
num_ways(9)
print(ways)
