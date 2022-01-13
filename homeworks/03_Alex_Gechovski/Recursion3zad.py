def replace_1(list_1,find,replace):

    if not isinstance(list_1,list) and not isinstance(list_1,tuple):
      return
    
    for i,value in enumerate(list_1): 
        if value == find:
           
            list_1[i] = replace
        elif isinstance(list_1, list) or isinstance(list_1,tuple):
           
            replace_1(value,find,replace)

        

list_1 = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
replace_1(list_1, 'a', 'c')
print(list_1) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]

