import sys
# add mzlat
def num_ways(steps):
    if steps <= 1:
        return 1
    return num_ways(steps-1) + num_ways(steps-2)

# sys.setrecursionlimit(1500)
print(num_ways(4))
