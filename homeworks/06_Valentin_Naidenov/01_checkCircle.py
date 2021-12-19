from math import sqrt

def check_Circles(c1_center, c1_rad, c2_center, c2_rad):
    if(c1_center == c2_center and c1_rad == c2_rad):
        return "Matching"
    c1_x, c1_y = c1_center
    c2_x, c2_y = c2_center

    distance = sqrt((c2_y - c1_y)**2 + (c2_x - c1_x)**2)
    rad_sum = c1_rad + c2_rad
    if(rad_sum < distance):
        return "not intesecting"
    if(rad_sum == distance):
        return "touching"
    if(rad_sum > distance):
        if(distance + c1_rad <= c2_rad):
            if(c1_rad + distance == c2_rad):
                return "Circle B contains circle A and they are touching"
            else:
                return "Circle B contains circle A"
        elif(distance + c2_rad <= c1_rad):
            if(c1_rad == c2_rad + distance):
                return "Circle A contains circle B and they are touching"
            else:
                return "Circle A contains circle B"
        else:
            return "intersecting"


a_c = (-7,5) 
b_c = (4,5)

a_r = 3
b_r = 14

print(check_Circles(a_c, a_r, b_c, b_r))
