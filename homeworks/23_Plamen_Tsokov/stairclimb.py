#zadacha 2#
while True:
	N = int(input("stair count: "))
	if N >= 2:
		break

def num_ways(N):
  if N < 2:
    return 1
  return num_ways(N-1) + num_ways(N-2)

print(num_ways(N))

