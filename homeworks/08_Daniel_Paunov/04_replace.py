
def replace(src, find, repl):
    new = []
    for x in src:
        if type(x) == list or type(x) == tuple:
            new.append(replace(x, find, repl))
        elif x == find:
            new.append(repl)
        else:
            new.append(x)

    return new
