N = input("Enter how many stairs you will climb: ")

def num_ways(n):
    
    if n < 0:
        return 0
        
    if n == 0:
        return 1

    nums = [0] * (n+1)
    nums[0] = 1
    nums[1] = 2

    for i in range(1, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

print(num_ways(int(N)))
