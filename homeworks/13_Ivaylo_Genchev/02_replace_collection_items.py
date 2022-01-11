"""
Задача 3:
Даден е Python списък от елементи - низове, числа, списъци (вкл. като този), наредени н-торки. Да се напише функция `replace` с 3 аргумента - `list`, `find`, `replace`,  където list e писък от типа по-горе, a find и replace са низове. Функцията връща нова версия на `list` в която всяко срещане на `find` e заменено  с `replace`.
Пример:
list = [ 'a', 1, [ ['a', 'b'], 1], ([1, 3, 'a'], 'b')]
res = replace(list, 'a', 'c')
print(res) # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]
"""


def replace(
    collection: list[str | int | list | tuple] | tuple[str | int | list | tuple],
    find: str | int,
    new: str | int,
) -> list[str | int | list | tuple] | tuple[str | int | list | tuple]:
    """Replace all occurances of 'find' in 'collection' with 'new'."""

    # copy list (preserve original as immutable)
    if isinstance(collection, list):
        new_collection = collection.copy()
    elif isinstance(collection, tuple):
        new_collection = list(collection)  # make tuple mutable
    else:
        raise ValueError(f"unsupported type: {type(collection)}")

    # iterate over all elements inside the list
    for i, element in enumerate(new_collection):
        # replace if element value is equal to find
        if element == find:
            new_collection[i] = new
        # if element is iterable, iterate over it the same way
        # since strings are iterable, they could cause infinite recursion
        elif hasattr(element, "__iter__") and not isinstance(element, str):
            if isinstance(element, tuple) or isinstance(collection, tuple):
                # convert element to tuple (if it has been converted to list)
                new_collection[i] = tuple(replace(element, find, new))
            else:
                new_collection[i] = replace(element, find, new)

    return new_collection


if __name__ == "__main__":
    collection: list[str | int | list | tuple] = [
        "a",
        1,
        [["a", "b"], 1],
        ([1, 3, "a"], "b"),
    ]
    find: str = "a"
    new: str = "c"

    res = replace(collection, find, new)
    print(f"Unchanged collection: {collection}")
    print(f"Having replaced '{find}' with '{new}': {res}")  # => [ 'c', 1, [ ['c', 'b'], 1], ([1, 3, 'c'], 'b')]
