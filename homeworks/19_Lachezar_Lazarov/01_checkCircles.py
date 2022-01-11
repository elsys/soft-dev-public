from math import sqrt

def checkCircle(c1_center, c1_rad, c2_center, c2_rad):
    if (c1_center == c2_center and c1_rad == c2_rad):
	    return "Matching"

    c1_x, c1_y = c1_center
    c2_x, c2_y = c2_center

    dist = sqrt((c1_x - c2_x)**2+(c1_y - c2_y)**2)
    sum_rad = c1_rad + c2_rad 

    if (dist < sum_rad):
        return "Intersecting"
    if (dist >sum_rad):
        return "Not intersecting"
    
    if(c1_rad + dist == c2_rad or c2_rad + dist == c1_rad):
        return "Containing!"

    if(dist == sum_rad):
        return "Touching"
    
c1_center = (2,0)
c1_rad = 1

c2_center = (1,1)
c2_rad = 2

print(checkCircle(c1_center,c1_rad,c2_center,c2_rad))
