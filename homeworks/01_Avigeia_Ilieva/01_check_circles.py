import math 

def check_circles(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0:
        return "MATCHING"
        
    elif distance == r1 + r2:
        return "TOUCHING"
        
    elif distance < r1 + r2:
        if distance > r1 or distance > r2:
            return "CONTAINING"
        else:   
            return "INTERSECTING"
            
    elif distance > r1 + r2:
        return "NO_COMMON"
        
    

