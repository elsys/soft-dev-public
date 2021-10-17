import math

def check_circles(c1_center, c1_rad, c2_center, c2_rad):

  a = c2_center[1] - c1_center[1]
  b = c2_center[0] - c1_center[0]
  c = math.sqrt(a**2 + b**2)
  print (c)

  if (c1_rad > c2_rad):
    rad = c1_rad - c2_rad
  else:
    rad = c2_rad - c1_rad

  if (c == c1_rad + c2_rad):
    return "Touching"
  elif (c == 0 and c1_rad == c2_rad):
    return "Matching"
  elif ((c1_rad + c2_rad) < c):
    return "Intersecting"
  elif (rad > c):
    return "Containing"
  else:
    return "Nothing in common"

print(check_circles((7,10), 5, (10,10), 9))
