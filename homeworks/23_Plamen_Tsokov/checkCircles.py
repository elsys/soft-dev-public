from math import sqrt

def check_Circles(c1_c, c1_r, c2_c, c2_r):
    if(c1_c == c2_c and c1_r == c2_r):
        return "Matching"
    c1_x, c1_y = c1_c
    c2_x, c2_y = c2_c

    distance = sqrt((c2_y - c1_y)**2 + (c2_x - c1_x)**2)

    if(c1_r + c2_ < distance):
        return "not intersecting"
    if(c1_r + c2_r == distance):
        return "touching"
    if(c1_r + c2_r > distance):
        if(distance + c1_r <= c2_r):
            if(c1_r + distance == c2_r):
                return "Circle B contains circle A and they are touching"
            else:
                return "Circle B contains circle A"
        elif(distance + c2_r <= c1_r):
            if(c1_r == c2_r + distance):
                return "Circle A contains circle B and they are touching"
            else:
                return "Circle A contains circle B"
        else:
            return "Intersecting"
