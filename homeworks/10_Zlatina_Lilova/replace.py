
def replace(list, old, new):
    index = 0
    for i in list:
        if type(i) != int and len(i) != 1:
            replace(list[index], old, new)                
        if i == old:
            list[index] = new
        
        index+=1

    return list

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 1, 'F')
print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]

