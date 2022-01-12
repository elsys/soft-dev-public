from typing import List


def replace(list, find, replace):
    for n, i in enumerate (list):
        """"
        if type(list[n]) is type(list):
            replace(list[n], find, replace)

        if type(list[n]) is tuple:
            replace(list[n], find, replace)
        """
        if i == find:
            list[n] = replace
        
    return list

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]

res = replace (list, 'a', 'c')
print(res)