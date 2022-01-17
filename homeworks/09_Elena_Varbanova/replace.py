def replace(listing, finding, replacing):
	counter = 0

	for index in listing:

		if type(index) != int and len(index) > 1:

			if type(index) == tuple:
				new_list = list(listing[counter])
				new_list = replace(new_list, finding, replacing)
				listing[counter] = tuple(new_list)
			
			else:
				new_list = listing[counter]
				new_list = replace(new_list, finding, replacing)

		if index == finding:
			listing[counter] = replacing

		counter = counter + 1 

	return listing


listing = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'a')]#last 'a' in English
res = replace(listing, 'a', 'c')
print(res)#[ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]

print("...........")

list1 = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'а')]#last 'a' in Bulgarian
res1 = replace(list1, 'a', 'c')
print(res1)#[ 2, 'e', [ ['a', 'b'], 'c'], (['e', 3, 2], 'a')]

print("...........")

list2 = [ 2, 1, [ ['a', 'b'], 'c'], ([1, 3, 2], 1)]
res2 = replace(list2, 1, 'e')
print(res2)#[ 2, 'e', [ ['a', 'b'], 'c'], (['e', 3, 2], 'b')]
