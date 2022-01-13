def replaceFunc(the_list, find, replace):
    if not isinstance(the_list, tuple) and not isinstance(the_list, list):
        if isinstance(the_list, str):
            if the_list == 'a':
                return 'c'
            else:
                return the_list
        
        return the_list
    
    new_list = []
    
    for i in range(len(the_list)):
        item = the_list[i]
        if isinstance(item, tuple):
            new_list.append(tuple(replaceFunc(item, find, replace)))
        else:
            new_list.append(replaceFunc(item, find, replace))

    return new_list


# tl = [2, 3, [2, 3, [7, 8], 2], (9,( 0,3, (4,5))), 1]
tl = ['a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]

nl = replaceFunc(tl, 'a', 'c')

print(tl)
print(nl)