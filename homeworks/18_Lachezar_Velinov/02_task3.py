def replace(List, Find, Replace):
    listCopy = list(List)

    for i, value in enumerate(listCopy): #go through list
        if value == Find:
            listCopy[i] = Replace #looks for value and replaces it

        elif type(value) in [list, tuple]:
            listCopy[i] = replace(listCopy[i], Find, Replace) #if container is found, goes inside it

    return listCopy


exampleList = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(exampleList, 'a', 'c')
print(res)
