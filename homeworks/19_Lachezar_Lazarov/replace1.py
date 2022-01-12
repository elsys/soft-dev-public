def replace1(list1, find, replace):
    for i in range(0, len(list1)):
        if list1[i] == find:
            list1[i] = replace
        try:
            if len(list1[i]) > 1:
                list1[i] = replace1(list1[i], find, replace)
        except:
            continue
    return list1
    
list1 = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace1(list1, 'a', 'c')
print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]
