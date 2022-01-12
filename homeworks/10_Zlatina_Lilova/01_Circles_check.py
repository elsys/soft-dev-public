import math
# the function returns the number of mutual points of the circles
def circle_check(radius1, radius2, center_1, center_2):
    a = center_1[1] - center_2[1]
    b = center_1[0] - center_2[0]
    
    c = math.sqrt(a*a + b*b)

    if(radius2 > radius1):
        rad = radius2 - radius1
    else:
        rad = radius1 - radius2

    position = 0
      
    if(c == 0 and radius2 == radius1):
        print("The circles are matching")
        position = 360
    elif(c == (radius1 + radius2)):
        print("The circles are touching")
        position = 1
    elif(c < rad):
        print("One circle contains the other")
        position = 0
    elif(c < (radius1 + radius2)):
        print("The circles are intersecting")
        position = 2
    else:
       print("The circles have no common") 

    return position    


print(circle_check(1,3, (111,11), (1,1)))
