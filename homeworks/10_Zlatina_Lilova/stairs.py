#solution: After trial and error I found that the ways of climbing up are a fibbonacci row;
#this means that the num of ways for a certain num of stairs is the corresponding fibbonaci number
# this is the reason we have 2 functions : one that finds the fibbonaci number and the main function 

#fibonacci function: recursively calls the function with the two number before it
#if the lowest number is reached, in our case 2 because thats the lowest value we can have, it returns the accumulated result
def fibonacci(num):
    if num <= 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

def num_ways(n):
    #error handling if the user entered wrong number
    if n < 2:
        return "INVALID ARGUMENT"
    num = n
    return fibonacci(num)

#tests
#print ("Number of ways = ", num_ways(1))
#print ("Number of ways = ", num_ways(3))
#print ("Number of ways = ", num_ways(2))
#print ("Number of ways = ", num_ways(4))

