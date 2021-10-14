from math import sqrt

def checkCircle(c1_center, c1_radius, c2_center, c2_radius):
	if c1_center == c2_center and c1_radius == c2_radius:
		return "The circles are matching"
	c1_x, c1_y = c1_center
	c2_x, c2_y = c2_center
	
	d = sqrt((c1_x - c2_x)**2+(c1_y - c2_y)**2)
	sum_of_radii = c1_radius + c2_radius
	
	if d == sum_of_radii:
		return "The circles touch"
	elif d < sum_of_radii:
		if d + c2_radius <= c1_radius:
			return "Circle one contains circle two"
		elif d + c1_radius <= c2_radius:
			return "Circle two contains circle one"
		else:
			return "The circles intersect"
	elif d > sum_of_radii:
		return "The circles do not intersect"

print(checkCircle((2,0),2,(2,0),1))
