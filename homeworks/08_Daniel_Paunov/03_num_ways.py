from math import comb

def num_ways(num):
    i = x = 0
    while x <= (num - x):
        i += comb(num - x, x)
        x += 1

    return i

for x in range(2, 10 + 1):
    print(str(x) + " : " + str(num_ways(x)))
