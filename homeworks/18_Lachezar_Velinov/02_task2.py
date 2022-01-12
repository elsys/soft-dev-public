from functools import lru_cache


@lru_cache(maxsize=10) #allows us to use 10 most recent values by caching them
def num_ways(n):
    if n <= 1:
        return n
    return num_ways(n-1) + num_ways(n-2)


print(num_ways(23))
