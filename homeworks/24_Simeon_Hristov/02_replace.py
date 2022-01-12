from copy import deepcopy
def replace_recursion(list, find, replace):
	for i in range(len(list)):
		if list[i] is find:
			list[i] = replace
		try:
			if len(list[i]) and not isinstance(list[i], str):
				list[i] = replace_recursion(list[i], find, replace)
		except:
			pass
	return list

def replace(list, find, replace):
	list_cpy = deepcopy(list)
	list_cpy = replace_recursion(list_cpy, find, replace)
	return list_cpy
