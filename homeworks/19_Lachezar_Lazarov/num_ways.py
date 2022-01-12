M = input("Stairs to climb: ")

def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)

print(num_ways(int(M)))
