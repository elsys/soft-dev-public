from math import sqrt

def check_circles(centre1, radius1, centre2, radius2):

    if(centre1 == centre2 and radius1 == radius2):
        return "Matching"

    x1, y1 = centre1
    x2, y2 = centre2
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    radius_sum = radius1 + radius2

    if(distance == radius_sum):
        return "Touching"
    
    if(distance < radius1 or distance < radius2):
        return "Containing"

    if(distance < radius_sum):
        return "Intercecting"

    if(distance > radius1 + radius2):
        return "No comman"
    

c1 = (1,1)
c2 = (-5, 6)
c1_rad = 1
c2_rad = 1

check_circles(c1,c1_rad,c2,c2_rad)