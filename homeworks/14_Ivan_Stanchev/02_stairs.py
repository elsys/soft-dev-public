N = int(input("Enter how many stairs you will climb: "))
while(N < 2):
    N = int(input("Enter how many stairs you will climb: "))

def num_ways(N):

    if N <= 2:
        return max(0, N)
    return num_ways(N-1) + num_ways(N-2)

print(num_ways(N))