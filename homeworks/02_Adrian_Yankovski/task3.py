l1st = ["a", "ab", "aa", "c"]
res = [] 
for find in l1st:
    replace = find.replace("a", "1")

    res.append(replace)


print(res)
