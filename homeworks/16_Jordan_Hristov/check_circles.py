from math import sqrt

def check_circles(c1, c1_rad, c2, c2_rad):

  c1_x, c1_y = c1
  c2_x, c2_y = c2
  d=sqrt((c2_y - c1_y)**2 + (c2_x - c1_x)**2)
  rad = c1_rad + c2_rad

  if (c1_rad > c2_rad):
    rad = c1_rad - c2_rad
  else:
    rad = c2_rad - c1_rad

  if (d == c1_rad + c2_rad):
    return "TOUCHING"
  elif (c1 == c2 and c1_rad == c2_rad):
    return "MATCHING"
  elif (rad > d):
    return "INTERESTING"
  elif (c1_rad + d == c2_rad or c2_rad + d == c1_rad):
    return "CONTACTING"
  elif (d > rad):
    return "NOTING IN COMMON"
  else:
    return "<3"
