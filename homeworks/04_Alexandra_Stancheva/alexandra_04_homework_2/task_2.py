def num_ways(N):
    first_num = 0
    second_num = 1
    ways = 0

    for i in range(1, (N + 1)):
        ways = first_num + second_num
        first_num = second_num
        second_num = ways

    return ways

stairs1 = 5
ways_for_stairs1 = num_ways(stairs1)
print(f'{stairs1} steps could be walked by {ways_for_stairs1} ways.\n')

stairs2 = 15
ways_for_stairs2 = num_ways(stairs2)
print(f'{stairs2} steps could be walked by {ways_for_stairs2} ways.\n')