list1 = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
def replace(list_values, find, replacement):

    for i in range(len(list_values)) :
        if (list_values[i]==find):
           list_values[i] = replacement

        if(  isinstance(list_values[i],(list,str,tuple)) == True and len(list_values[i])>1):
            if(type(list_values[i]) is tuple):
                temp_list = list(list_values[i])
                temp_list = replace(temp_list,find,replacement)
                list_values[i] = tuple(temp_list)
            else: 
                list_values[i] = replace(list_values[i],find,replacement)

    return list_values

rep =  replace(list1,'b','c')

print(rep)
