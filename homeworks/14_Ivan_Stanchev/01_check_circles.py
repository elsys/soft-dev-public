from math import sqrt

def check_circles(c1_center, c1_radius, c2_center, c2_radius):
    x1, y1 = c1_center
    x2, y2 = c2_center
    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    sum_of_radii = c1_radius + c2_radius

#MATCHING
    if(c1_center == c2_center and c1_radius == c2_radius):
        return "MATCHING"

# TOUCHING
    if d == sum_of_radii:
        return "TOUCHING"        
    elif d < sum_of_radii:

# CONTAINING
        if d + c2_radius <= c1_radius:
            return "First circle contains second one"

        elif d + c1_radius <= c2_radius:
			return "Second circle contains first one"

# INTERSECTING
        else:
			return "INTERSECTING"
# NO_COMMON
    elif d > sum_of_radii:
		return "NO_COMMON"

	elif d < sum_of_radii:
		if d + c2_radius <= c1_radius:
		  return "Circle one contains circle two"
		elif d + c1_radius <= c2_radius:
			return "Circle two contains circle one"
