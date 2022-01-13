print("How many stairs would you like to climb? ")
x=input()

def fibonacci_number(N):
    if N<=1:
        return N
    return fibonacci_number(N-1) + fibonacci_number(N-2)
 
    
def num_ways(N):
    return fibonacci_number(N+1)
