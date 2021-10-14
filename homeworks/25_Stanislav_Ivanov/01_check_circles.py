class IncorrectDataTypeError(Exception):
    """Custom exception raised when datatype for either center or radius of a circle is incorrect."""

    def __init__(self, required_type):
        self.message = f"Received incorrect data type, expected: {required_type}."
        super().__init__(self.message)


class NotPointError(Exception):
    """Custom exception raised when a tuple with coordinates for center of a circle has more or less than 2 elements."""

    def __init__(self, message):
        super().__init__(message)


class NonPositiveValueError(Exception):
    """Custom exception raised when value of a radius is nonpositive."""

    def __init__(self, message):
        super().__init__(message)


def calculate_distances(point_a, point_b):
    """Calculate distances between two points"""
    dx = point_a[0] - point_b[0]
    dy = point_a[1] - point_b[1]
    return (dx**2 + dy**2) ** 0.5


def check_circles(c1_center, c1_radius, c2_center, c2_radius):
    """Check state of circles"""

    # Handle incorrect type of data
    if type(c1_center) != tuple or type(c2_center) != tuple:
        raise IncorrectDataTypeError("tuple")
    if type(c1_radius) != int or type(c2_radius) != int:
        raise IncorrectDataTypeError("int")

    # Handle incorrect values
    if len(c1_center) != 2 or len(c2_center) != 2:
        raise NotPointError("A point should have 2 coordinates.")
    if c1_radius <= 0 or c2_radius <= 0:
        raise NonPositiveValueError("Radius of a circle should be a positive number")

    # check state of circles
    if c1_center == c2_center and c1_radius == c2_radius:
        return "MATCHING"
    distance = calculate_distances(c1_center, c2_center)
    if distance == c1_radius + c2_radius:
        return "TOUCHING"
    if distance > c1_radius + c2_radius:
        return "NO COMMON"
    if distance < c1_radius + c2_radius:
        return "INTERCECTING"
    if distance <= abs(c1_radius - c2_radius):
        return "CONTAINING"
