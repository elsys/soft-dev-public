import math

def take_distance(point1, point2):
    a = point1[0] - point2[0]
  
    b = point1[1] - point2[1]
    return math.sqrt( a*a + b*b)

def check_containment(c1_center,c2_center,c1_raduis,c2_radius):
    flag = True
    if not c1_raduis > 2*c2_radius:

        flag = False
    elif not c1_raduis - c1_center[0]> c2_radius - c2_center[0]:
        flag = False
    elif not c1_raduis - c1_center[1]> c2_radius - c2_center[1]:
        flag = False

    return flag
             
def check_circles(c1_center,c2_center,c1_raduis,c2_radius):
    if c1_center == c2_center and c1_raduis == c2_radius:
        return "MATCHING"

    elif check_containment(c1_center,c2_center,c1_raduis,c2_radius) == True or check_containment(c2_center,c1_center,c2_radius,c1_raduis) == True:
        return "CONTAINING"
    else:
        if (c1_raduis + c2_radius) < take_distance(c1_center,c2_center):
            return "NOTCOMMON"
        elif (c1_raduis + c2_radius) == take_distance(c1_center,c2_center):
            return "TOUCHING"
        elif (c1_raduis + c2_radius) > take_distance(c1_center,c2_center):
            return "INTERSECTING"

    

circle1_cordinates = (2,2)
circle2_cordinates = (0,0)


answer = check_circles(circle1_cordinates,circle2_cordinates, 2, 5)

print (answer)
