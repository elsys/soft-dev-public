def num_ways(N):
    if N < 2:
        return 'too few steps' 
    n1, n2 = 0, 1
    i = 0;
    while i < N :
        ways = n1 + n2
        n1 = n2
        n2 = ways
        i += 1
    return ways

#examples
print (num_ways(3))
print (num_ways(5))





