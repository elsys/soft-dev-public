
def replace(current_list, find, replacement):
    for i in range(0, len(current_list)):
        if isinstance(current_list[i], list):
            replace(current_list[i], find, replacement)

        if type(current_list[i]) is tuple:
            new_list = list(current_list[i])
            replace(new_list, find, replacement)
            current_list[i] = tuple(new_list)

        if current_list[i] == find:
             current_list[i] = replacement



my_list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]

replace(my_list, 'a', 'c')

print(my_list)
