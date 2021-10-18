from math import sqrt

def circle(center_1, radius_1, center_2, radius_2);

    a1, b1 = center_1;
    a2, b2 = center_2;
    distance_between = sqrt((a1 - a2)**2 + (b1 - b2)**2);
    radius = (r1 + r2)**2;

    if (center_1 == center_2 and radius_1 == radius_2):
		return "MATCHING"

    if (distance_between == radius):
        return "TOUCHING"

    if (distance_between > radius_1 + radius_2):
        return "DO NOT INTERSECT"

    if (distance_between < radius_1 + radius_2):
        return "INTERSECTING"

    if ( radius_1 + distance_between == radius_2 || radius_2 + distance_between == radius_1):
        return "CONTAINING"
