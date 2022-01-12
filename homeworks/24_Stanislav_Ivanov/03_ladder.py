def num_ways(steps: int) -> int:
    if type(steps) is not int:
        raise TypeError("n must be an integer")

    if steps <= 2:
        return max(0, steps)
    return num_ways(steps-1) + num_ways(steps-2)


if __name__ == "__main__":
    print(num_ways(2))
    print(num_ways(3))
    print(num_ways(4))
    print(num_ways(-3))
    try:
        print(num_ways("5"))
    except TypeError as error:
        print(error)
