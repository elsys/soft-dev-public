# =============================================================================================== #
# Classes, Functions, Global variables #


def replace(a_list, to_find, replace_with):
	list_copy = list(a_list)	# copy so that we don't modify the passed list

	for i, value in enumerate(list_copy):
		if value == to_find:
			# Found a value to replace
			list_copy[i] = replace_with
		elif type(value) in [list, tuple]:
			# Found another collection => iterate through it recursively
			list_copy[i] = replace(list_copy[i], to_find, replace_with)
	
	return list_copy


# =============================================================================================== #


def main():

	# Examples
	list = [ 'a', 1, [['a', 'b'], 1], ([1, 3, 'a'], 'b')]
	res = replace(list, 'a', 'c')
	print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]


# =============================================================================================== #


if __name__ == "__main__":
	main()
