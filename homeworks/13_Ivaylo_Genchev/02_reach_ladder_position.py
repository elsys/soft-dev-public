from inspect import get_annotations  # type check function arguments
from sys import (
    version_info,
)  # check python version (differt ways to type check annotations)

"""
Дадена е стълба с N >= 2 стъпала. Стоим в началото на стълбата и можем да качим 1 или 2 стъпала наведнъж. 
Да се напише функция, `num_ways` която по подадено N връща броя на начини по които можем да изкачим стълбата - т.е. да стъпим на N-тото стъпало.
Пример: при N = 2 функцията връща 2 - можем да минем по всяко стъпало (начин 1) или да се качим директно на второто (начин 2)
при N=3 функцията връща 3 - можем да качим трите стъпала едно по едно (начин 1), да изкачим 1 стъпало и осналите наведнъж (начин 2) или да изкачим първите 2 стъпала наведнъж и после третото (начин 3)
"""


def num_ways(steps: int) -> int:
    """
    Function to calculate the amount of different ways a ladder can be climbed to the nth step.
    Acts as an error handler.
    """

    # N cannot be less than 2 (according to task requirement)
    if steps < 2:
        raise ValueError(
            f"Invalid input '{steps}'. Amount of steps to climb must be greater than 1."
        )

    if version_info[1] < 10:  # get minor python version (for type checking)
        if (
            type(steps) != num_ways.__annotations__["steps"]
        ):  # PEP compliant way to access annotations before 3.10
            raise TypeError(f"Argument 'steps' cannot be of type {type(steps)}.")
    else:  # 3.10+
        if (
            type(steps) != get_annotations(num_ways)["steps"]
        ):  # PEP compliant way to access annotatinos (3.10+)
            raise TypeError(f"Argument 'steps' cannot be of type {type(steps)}.")

    def calculate_ways(remaining_steps: int, ways_amount: int = 0) -> int:
        """Recursively calculate the amount of ways N steps can be climbed."""

        # exit condition
        if (
            remaining_steps < 0
        ):  # don't change ways_amount due invalid movement (1 step was remaining but 2 were climbed)
            return ways_amount
        elif remaining_steps == 0:
            return ways_amount + 1

        # try to climb steps 1 and 2 at a time
        ways_amount = calculate_ways(remaining_steps - 1, ways_amount)
        ways_amount = calculate_ways(remaining_steps - 2, ways_amount)

        return ways_amount

    return calculate_ways(steps)


def fibonacci(n: int) -> int:
    """
    Calculate the next fibonacci number.
    Could be faster if a precomputed dict of the fibonacci sequence is used.
    """

    # type check
    if version_info[1] < 10:  # get minor python version (for type checking)
        if (
            type(n) != fibonacci.__annotations__["n"]
        ):  # PEP compliant way to access annotations before 3.10
            raise TypeError(f"Argument 'n' cannot be of type {type(n)}.")
    else:  # 3.10+
        if (
            type(n) != get_annotations(fibonacci)["n"]
        ):  # PEP compliant way to access annotations (3.10+)
            raise TypeError(f"Argument 'n' cannot be of type {type(n)}.")

    first: int = 0
    second: int = 1

    if n < 1:
        raise ValueError(f"Nth fibonacci number cannot be {n}. Has to be > 1!")
    elif n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(1, n):
            result: int = first + second
            first = second
            second = result

        return second


if __name__ == "__main__":
    step: int = 5
    print(f"Standard recursion sollution: {num_ways(step)}")
    print(
        f"Using fibonacci sequence (better performance): {fibonacci(step+1)}"
    )  # step+1 because first fibonacci number is 0, essentially callibrating the function
