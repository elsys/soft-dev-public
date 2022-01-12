def replace(l, find, replacer):
  try:
    l = l.copy()
    for i, item in enumerate(l):
        if item == find:
            l[i] = replacer
            continue
        elif type(l[i]) is tuple:
          l[i] = list(l[i])
          for i, item in enumerate(l):
            if item == find:
              l[i] = replacer
        l[i] = replace(item, find, replacer)
  finally:
      return l


l = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(l, 'a', 'c')
print(res)