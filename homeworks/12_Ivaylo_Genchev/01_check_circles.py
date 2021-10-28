from math import sqrt


class NegativeRadiusError(Exception):
    """Custom exception raised when circle radius is negative."""

    def __init__(self) -> None:
        super().__init__("Circle radius is negative.")


class InvalidDataType(Exception):
    """Custom exception raised when circle coordinates or radius aren't of type int or float."""

    def __init__(self, message: str = "") -> None:
        super().__init__(f"Invalid data type. {message}")


def get_distance(
    c1_center: tuple[float | int, float | int],
    c2_center: tuple[float | int, float | int],
) -> float:
    """Calculates the distance between 2 circle centers."""

    return sqrt((c1_center[0] - c2_center[0]) ** 2 + (c1_center[1] - c2_center[1]) ** 2)


def check_circles(
    c1_center: tuple[float, float],
    c1_radius: float,
    c2_center: tuple[float, float],
    c2_radius: float,
) -> str:

    # Handle incorrect data types
    if type(c1_center) != tuple or type(c2_center) != tuple:
        raise InvalidDataType(f"Expected tuple.")
    if type(c1_center[0]) != int and type(c1_center[0]) != float:
        raise InvalidDataType(
            f"Expected int or float. Not {type(c1_center[0])}")
    if type(c1_center[1]) != int and type(c1_center[1]) != float:
        raise InvalidDataType(
            f"Expected int or float. Not {type(c1_center[1])}")
    if type(c2_center[0]) != int and type(c2_center[0]) != float:
        raise InvalidDataType(
            f"Expected int or float. Not {type(c2_center[0])}")
    if type(c2_center[1]) != int and type(c2_center[1]) != float:
        raise InvalidDataType(
            f"Expected int or float. Not {type(c2_center[1])}")
    if type(c1_radius) != int and type(c1_radius) != float:
        raise InvalidDataType(f"Expected int or float. Not {type(c1_radius)}")
    if type(c2_radius) != int and type(c2_radius) != float:
        raise InvalidDataType(f"Expected int or float. Not {type(c2_radius)}")

    # Handle negative radius
    if c1_radius < 0 or c2_radius < 0:
        raise NegativeRadiusError

    def are_matching() -> bool:
        """
        Checks if 2 circles are matching.
        Both circles must share all points.
        """

        # check if the 2 circles have matching coordinates and radius
        if c1_center == c2_center and c1_radius == c2_radius:
            return True

        # the circles aren't matching
        return False

    def are_nested() -> bool:
        """Checks if one of the circles is fully consumed by the other."""

        # check if the distance between the 2 circles + the firsts radius is less than the seconds radius
        if circle_dist + c1_radius < c2_radius or circle_dist + c2_radius < c1_radius:
            return True

        # the circles aren't nested
        return False

    def are_touching() -> bool:
        """
        Checks if 2 circles are touching.
        Both circles must share 1 point.
        """

        # check if the distance between the circles is equal to their combined radius
        if circle_dist == c1_radius + c2_radius:
            return True

        # the circles aren't touching
        return False

    def are_intersecting() -> bool:
        """Checks if the 2 circles have more than 1 touching point."""

        # check if the distance between the 2 circles is less than their combined radius
        if circle_dist < c1_radius + c2_radius:
            return True

        # the circles aren't intersecting
        return False

    circle_dist = get_distance(c1_center, c2_center)

    if are_matching():
        return "MATCHING"
    elif are_nested():
        return "CONTAINING"
    elif are_intersecting():
        return "INTERSECTING"
    elif are_touching():
        return "TOUCHING"

    return "NO COMMON"


if __name__ == "__main__":

    print(check_circles((2.6, 7), 2, (2.6, 7), 2))  # MATCHING
    print(check_circles((0, 0), 5, (12, 9), 10))  # TOUCHING
    print(check_circles((0, 0.2), 100.3, (5, 5), 19.2))  # CONTAINING
    print(check_circles((0, 0), 5, (3, 3), 3))  # INTERSECTING
    print(check_circles((0, 0), 1, (10, 10), 1))  # NO COMMON
