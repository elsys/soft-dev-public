from __future__ import annotations

from math import sqrt

"""
Assignment:

Given 2 circles in 2d space:
Params: center point cordinates(x, y), radius size
Task: Determine their state - matching, touching, nested, intersecting, unrelated.
"""

class NegativeRadiusError(Exception):
    """Custom exception raised when circle radius is negative."""

    def __init__(self) -> None:
        super().__init__("Circle radius is negative.")

class InvalidDataType(Exception):
    """Custom exception raised when circle cordinates or radius aren't of type int or float"""

    def __init__(self) -> None:
        super().__init__("Invalid data type. Expected integer or float.")


class Circle:
    def __init__(self, x: float, y: float, r: float) -> None:

        if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float) or (type(r) != int and type(r) != float):
            raise InvalidDataType()            

        if r < 0: 
            raise NegativeRadiusError() 
        
        self.cords = (x, y)
        self.radius = r

    def get_distance(self, other_circle: Circle) -> float:
        """Calculates the distance between 2 circle centers."""

        # calculate distance between 2 points (Pythagorean theorem)
        return sqrt((self.cords[0] - other_circle.cords[0])**2 + (self.cords[1] - other_circle.cords[1])**2)


    def is_matching(self, other_circle: Circle) -> bool:
        """
        Checks if 2 circles are matching.
        Both circles must share all points.
        """

        # check if the 2 circles have matching cordinates and radius
        if self.cords[0] == other_circle.cords[0] and self.cords[1] == other_circle.cords[1] and self.radius == other_circle.radius:
            return True

        # the circles aren't matching
        return False

    def is_touching(self, other_circle: Circle, _dist: None) -> bool:
        """
        Checks if 2 circles are touching.
        Both circles must share 1 point.
        """

        dist = _dist if _dist is not None else self.get_distance(other_circle)

        # check if the distance between the circles is equal to their combined radius
        if dist == self.radius + other_circle.radius:
            return True
        
        # the circles aren't touching
        return False

    def is_nested(self, other_circle: Circle, _dist: None) -> bool:
        """Checks if this->circle is fully consumed by another cirlce without the 2 circles touching."""
        
        dist = _dist if _dist is not None else self.get_distance(other_circle)

        # check if the distance between the 2 circles + the firsts radius is less than the seconds radius
        if dist + self.radius < other_circle.radius:
            return True
        
        # this circle isn't nested in other_circe
        return False

    def is_tangent(self, other_circle: Circle, _dist: None) -> bool:
        """Checks if this->circle is fully consumed by another cirlce with the 2 circles touching."""

        dist = _dist if _dist is not None else self.get_distance(other_circle)

        # check if the distance between the 2 circles + the firsts radius is the same as the second circles radius
        if dist + self.radius == other_circle.radius:
            return True
        
        # this circle isn't tangent to the other_circle
        return False

    def is_intersecting(self, other_circle: Circle, _dist: None) -> bool:
        """Checks if the 2 circles have more than 1 touching point."""

        dist = _dist if _dist is not None else self.get_distance(other_circle)

        # check if the distance between the 2 circles is less than their combined radius 
        if dist < self.radius + other_circle.radius:
            return True

        # the circles aren't intersecting
        return False

    def is_unrelated(self, other_circle: Circle, _dist: None) -> bool:
        """Checks if the 2 circles are unrelated (aren't in any other sate)."""

        dist = _dist if _dist is not None else self.get_distance(other_circle)

        # check if the distance between the 2 circles is greater than their combined radius
        if dist > self.radius + other_circle.radius:
            return True

        # the circles aren't unrelated
        return False

    def get_state(self, other_circle: Circle) -> int:
        """
        Returns an integer corresponding to the 2 circles state:
            0 - the 2 circles are matching.
            1 - the 2 circles are touching.
            2 - this circle is nested in other_circle.
            3 - this circle is tangent to other_circle.
            4 - the 2 circles are intersecting.
            -1 - the 2 circles are unrelated.
        """

        if self.is_matching(other_circle):
            print("The circles are matching")
            return 0

        # Calculate distance once (sqrt can be expensive)
        dist = self.get_distance(other_circle)

        if self.is_touching(other_circle, dist):
            print("The circles are touching")
            return 1

        if self.is_nested(other_circle, dist):
            print("This circle is nested in the other cirlce")
            return 2

        if self.is_tangent(other_circle, dist):
            print("This circle is tangent to the other circle")
            return 3

        if self.is_intersecting(other_circle, dist):
            print("The circles are intersecting")
            return 4

        print("The circles are unrelated")
        return -1


"""Tests: (don't catch custom exceptions for debug purposes)"""

# matching
a = Circle(2.6, 7, 2)
b = Circle(2.6, 7, 2)
print(a.get_state(b))  # 0

# touching
a = Circle(0, 0, 5)
b = Circle(12, 9, 10)
print(a.get_state(b))  # 1

# nested
b = Circle(0, 0.2, 100.3)
a = Circle(5, 5, 20)
print(a.get_state(b))  # 2

# tangent
b = Circle(0, 0, 100)
a = Circle(0, 80, 20)
print(a.get_state(b))  # 3

# intersecting
a = Circle(0, 0, 5)
b = Circle(3, 3, 3)
print(a.get_state(b))  # 4

# unrelated
a = Circle(0, 0, 1)
b = Circle(10, 10, 1)
print(a.get_state(b))  # -1
