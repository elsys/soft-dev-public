def replace(list, find, change):

    counter = 0
    for i in list:
        if type(i) != int:
            if len(i) > 1:
                replace(list[counter], find, change)

        if list[counter] == find:
            list[counter] = change
        counter = counter + 1
    return list

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res)
