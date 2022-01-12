import time


# =============================================================================================== #
# Classes, Functions, Global variables #


def num_ways(N, found):
	# Optimized with memoization

	if N in found:
		return found[N]

	if N <= 1: return 1

	num = num_ways(N - 1, found) + num_ways(N - 2, found)
	found[N] = num

	return num



# =============================================================================================== #


def main():

	start_time = time.time()
	dict = {}

	# Examples
	print("Ways to climb a ladder with {} steps: {}".format(2, num_ways(2, dict)))
	print("Ways to climb a ladder with {} steps: {}".format(3, num_ways(3, dict)))
	print("Ways to climb a ladder with {} steps: {}".format(5, num_ways(5, dict)))
	print("Ways to climb a ladder with {} steps: {}".format(7, num_ways(7, dict)))

	# print("Ways to climb a ladder with {} steps: {}".format(100, num_ways(200, dict)))

	print("\n### Completed after {:.6f} seconds ###".format(time.time() - start_time))


# =============================================================================================== #


if __name__ == "__main__":
	main()
