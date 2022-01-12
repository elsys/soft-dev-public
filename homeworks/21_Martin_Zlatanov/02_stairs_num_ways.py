def fibonacci(i):
  if i == 1 or i == 2:
    return i
  return fibonacci(i-1) + fibonacci(i-2)
  

def num_ways(N):
  if N <= 1:
    return "Error"
  elif N == 2:
      return N
  return fibonacci(N)
    

print(num_ways(3))
print(num_ways(4))
print(num_ways(0))
