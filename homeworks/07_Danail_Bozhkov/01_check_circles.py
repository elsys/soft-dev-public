from math import sqrt

def checkCircles(c1, r1, c2, r2):

    if(c1 == c2 and r1 == r2):
        print("Matching")
        return

    x1, y1 = c1
    x2, y2 = c2
    Distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    Radius_sum = r1 + r2

    if(Distance == Radius_sum):
        print("Touching")
        return
    if(Distance < r1 or Distance < r2):
        print("Containing")
        return
    if(Distance < Radius_sum):
        print("Intercecting")
        return
    if(Distance > r1 + r2):
        print("No comman")
        return
    

c1 = (1,1)
c2 = (-5, 6)
c1_rad = 1
c2_rad = 1

checkCircles(c1,c1_rad,c2,c2_rad)
