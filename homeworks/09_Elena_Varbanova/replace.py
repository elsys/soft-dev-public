def replace(list, finding, replacing):
	counter = 0

	for index in list:

		if type(index) != int and len(index) > 1:
			new_list = list[counter]
			replace(new_list, finding, replacing)

		if index == finding:
			list[counter] = replacing
		counter = counter + 1 

	return list


list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res)#[ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]

print("...........")

list1 = [ 2, 1, [ ['a', 'b'], 'c'], ([1, 3, 2], 'b')]
res1 = replace(list1, 1, 'e')
print(res1)#[ 2, 'e', [ ['a', 'b'], 'c'], (['e', 3, 2], 'b')]
