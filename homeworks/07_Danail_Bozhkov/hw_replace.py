from typing import Any

def replace(element: Any, find: str, replace: str):
    if element == find:
        return replace

    for i in range(len(element)):
        if element[i] == find:
            element[i] = replace
    
    return element
   

list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res)
