
def distance(c1_center, c2_center):
    return ((float(c1_center[0]) - float(c2_center[0])) ** 2 + (float(c1_center[1]) - float(c2_center[1])) ** 2) ** 0.5

def checkCircles(c1_center, c1_radius, c2_center, c2_radius):
    if float(c1_radius) < float(c2_radius):
        temp_center = c1_center
        temp_radius = float(c1_radius)
        c1_center = c2_center
        c1_radius = float(c2_radius)
        c2_center = temp_center
        c2_radius = float(temp_radius)
    if c1_center == c2_center and float(c1_radius) == float(c2_radius):
        return "Matching"
    elif distance(c1_center, c2_center) + float(c2_radius) < float(c1_radius):
        return "Containing"
    elif distance(c1_center, c2_center) == float(c1_radius) + float(c2_radius):
        return "Touching"
    elif distance(c1_center, c2_center) < float(c1_radius) + float(c2_radius):
        return "Intersecting"
    else:
        return "Non-matching"
    return

while True:
    try:
        c1_center_in = input("Circle 1 center (x, y): ")

        if ',' in c1_center_in:
            if ' ' in c1_center_in:
                c1_center_in = c1_center_in.split(',')
                c1_center = c1_center_in[0]
                c1_center += c1_center_in[1]
                c1_center = c1_center.split(' ')
                c1_center = tuple(c1_center)
            else:
                c1_center = tuple(c1_center_in.split(','))

        else:
            c1_center = tuple(c1_center_in.split(' '))

        float(c1_center[0]) == float(c1_center[1])

    except ValueError:
        print("Error: Failed to parse input.\nMust be 2 numbers separated by a space and/or comma.")
        continue

    break

while True:
    try:
        c1_radius_in = input("Circle 1 radius (r): ")

        c1_radius = float(c1_radius_in)

        if c1_radius <= 0:
            print("Error: Radius must be positive.")
            continue

    except ValueError:
        print("Error: Failed to parse input.\nMust be a positive number.")
        continue

    break

while True:
    try:
        c2_center_in = input("Circle 2 center (x, y): ")

        if ',' in c2_center_in:
            if ' ' in c2_center_in:
                c2_center_in = c2_center_in.split(',')
                c2_center = c2_center_in[0]
                c2_center += c2_center_in[1]
                c2_center = tuple(c2_center.split(' '))
            else:
                c2_center = tuple(c2_center_in.split(','))

        else:
            c2_center = tuple(c2_center_in.split(' '))

        float(c2_center[0]) == float(c2_center[1])

    except ValueError:
        print("Error: Failed to parse input.\nMust be 2 numbers separated by a space and/or comma.")
        continue

    break

while True:
    try:
        c2_radius_in = input("Circle 2 radius (r): ")

        c2_radius = float(c2_radius_in)

        if c2_radius <= 0:
            print("Error: Radius must be positive.")
            continue

    except ValueError:
        print("Error: Failed to parse input.\nMust be a positive number.")
        continue

    break

print(checkCircles(c1_center, c1_radius, c2_center, c2_radius))
