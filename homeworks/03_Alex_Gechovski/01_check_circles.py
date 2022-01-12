from math import sqrt

def check_circles(c1_cen, c1_rad , c2_cen , c2_rad):
    
    c1_x, c1_y = c1_cen
    c2_x, c2_y = c2_cen

    distance = sqrt((c2_y - c1_y)**2 + (c2_x - c1_x)**2)
    
    if(c1_cen == c2_cen and c1_rad == c2_rad):
        return "Matching!"
    
    if(c1_rad + c2_rad < distance):
        return "Not Intersecting!"
    
    if(c1_rad + c2_rad == distance):
        return "Touching!"
    
    if(c1_rad + c2_rad > distance):
        
        if(c1_rad + distance == c2_rad or c2_rad + distance == c1_rad):
            return "Containing!"
        
        else:
            return "Intercepting!"

a_c = (2,0) 
b_c = (0,0)

a_r = 3
b_r = 1

print(check_circles(a_c, a_r, b_c, b_r))
