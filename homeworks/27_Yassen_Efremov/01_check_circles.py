import math

# A function that returns information about two given circles in a cartesian coordinate system
def checkCircles(c1_center, c1_radius, c2_center, c2_radius):

	# Calculate the distance here because we use it a lot later
	center_distance = math.sqrt((c2_center[0] - c1_center[0])**2 + (c2_center[1] - c1_center[1])**2)

	# No common
	if center_distance > c1_radius + c2_radius:
		return "no common"

	elif center_distance < c1_radius + c2_radius:
		# Matching
		if not center_distance and c1_radius == c2_radius: return "matching"
		# Touching (from the inside)
		if c1_radius == center_distance + c2_radius or c2_radius == center_distance + c1_radius: return "touching"
		# Containing
		if c1_radius > center_distance + c2_radius: return "c1 contains c2"
		if c2_radius > center_distance + c1_radius: return "c2 contains c1"
		# Intersecting
		return "intersecting"

	else:	# Touching
		return "touching"



# Example of two intersecting circles
print(checkCircles([0, 1], 2, [2, 1], 3))
# Example of two touching circles
print(checkCircles([-2, 0], 2, [1, 0], 1))
# Example of two containing circles
print(checkCircles([0, 2], 4, [2, 0], 1))
