def fibonacci(number):
	if number <= 1:
		return number
	return fibonacci(number - 1) + fibonacci(number - 2)


def num_ways(num):
	return fibonacci(num + 1)


stair1 = 2
print("Number of ways:", num_ways(stair1))

stair2 = 3
print("Number of ways:", num_ways(stair2))

stair3 = 4
print("Number of ways:", num_ways(stair3))
