from math import sqrt


def calc_distance(center1, center2):
    diff_x = center1[0] - center2[0]
    diff_y = center1[1] - center2[1]
    return sqrt(diff_x**2 + diff_y**2)


def check_cicles(center1, radius1, center2, radius2):
    if center1 == center2 and radius1 == radius2:
        return "MATCHING"

    distance = calc_distance(center1, center2)

    if distance < radius1 - radius2 or distance < radius2 - radius1:
        return "CONTAINING"

    if distance < radius1 + radius2:
        return "INTERSECTING"

    if distance > radius1 + radius2:
        return "NO_COMMON"

    if distance == radius1 + radius2:
        return "TOUCHING"


if __name__ == "__main__":
    test_center1 = (2, 5)
    test_radius1 = 4

    test_center2 = (2, 5)
    test_radius2 = 4

    print(check_cicles(test_center1, test_radius1, test_center2, test_radius2))
