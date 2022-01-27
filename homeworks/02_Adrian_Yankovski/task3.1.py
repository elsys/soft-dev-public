def replace(listt,find,replac):

    if not isinstance(listt,list) and not isinstance(listt,tuple):
      return

    for i,value in enumerate(listt): 
        if value == find:

            listt[i] = replac
        elif isinstance(listt, list) or isinstance(listt,tuple):

            replace(value,find,replac)
    return listt


newlist = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]

res = replace(newlist, 'a', 'c')

print(res)
