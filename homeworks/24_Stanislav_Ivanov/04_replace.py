from typing import Any


def replace(element: Any, find: str, replace_: str) -> Any:
    if element == find:
        return replace_
    element_type = type(element)
    try:
        if type(element) is str:
            return element
        element = list(element)
        for index in range(len(element)):
            element[index] = replace(element[index], find, replace_)
    finally:
        return element_type(element)


if __name__ == "__main__":
    test_list = [1, "2", 3, "45", "7", [1, "2"], (1, ["2", "34"], 3, "2")]
    print(replace(test_list, "2", "99"))
