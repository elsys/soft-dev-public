import math

def checkCircles(c1_center, c1_radius, c2_center, c2_radius):
	diameter = math.sqrt((c2_center[0] - c1_center[0])**2 + (c2_center[1] - c1_center[1])**2)
	sum_raduises = c1_radius + c2_radius
	if c1_center == c2_center and c1_radius == c2_radius:
		return "Matching"
	if diameter == sum_raduises:
		return "Touching"
	if diameter + c1_radius <= c2_radius:
		return "Circle 2 contains circle 1"
	if diameter + c2_radius <= c1_radius:
		return "Circle 1 contains circle 2"
	if sum_raduises < diameter:
		return "Intersecting"
	else:
		return "No common"
#Example for matching circles
print(checkCircles((3,3), 5, (3,3), 5))
#Example for touching circles
print(checkCircles((2,4), 2, (5,4), 1))
#Example for circle 2 containing circle 1
print(checkCircles((2,2), 5, (3,3), 7))
#Example for circle 1 containing circle 2
print(checkCircles((6,6), 8, (4,4), 4))
#Example for intersecting circles
print(checkCircles((3,3), 5, (9,9), 3))
#Example for no common circles
print(checkCircles((3,3), 5, (8,9), 3))