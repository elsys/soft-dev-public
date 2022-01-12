def replace(list, find, replacee):
	counter = 0
	for i in list:
		if (type(i) != int) and (len(i) > 1):
			list2 = list[counter]
			replace(list2, find, replacee)
		if i == find:
			list[counter] = replacee
		counter = counter + 1 
	return list

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]