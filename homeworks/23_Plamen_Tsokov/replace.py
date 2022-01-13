#zadacha 3#
def replace(list, find, replace1):
	a = 0
	for i in list:
		if (type(i) != int) and (len(i) > 1):
			list2 = list[a]
			replace(list2, find, replace1)
		if i == find:
			list[a] = replace1
		a = a +1 
	return list

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]

