def replace(listt, find, replace):
    list2=list(listt)
    for i, value  in enumerate(list2):
        if listt[i] == find:
            listt[i] = replace

        elif type(value) in[list, tuple]:
            list2[i]=replace(list2[i], find, replace)
                                 
        return list2

exampleList = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(exampleList, 'a', 'c')
print(res)
