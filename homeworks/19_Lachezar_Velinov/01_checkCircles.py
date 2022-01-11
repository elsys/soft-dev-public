import math

class Circle:
    def __init__(self, x, y, rad): # a constructor for the circle class
        self.x = x
        self.y = y
        self.rad = rad
        
        
# the abs function is equal to a module in mathematics.
def find_centre_distance(Circle1, Circle2):
    x_axis = abs(Circle1.x - Circle2.x)
    y_axis = abs(Circle1.y - Circle2.y)
    
    if(x_axis == 0 and y_axis == 0):
        distance = 0
    else:
        distance = math.sqrt((x_axis**2) + (y_axis**2)) # using the Pythagorean theorem to find the distance between the 2 centres
    
    
    if(distance > (Circle1.rad + Circle2.rad)):
        print("No common")
    elif(distance < (Circle1.rad + Circle2.rad)):
        if(distance == 0 and Circle1.rad == Circle2.rad):
            print("Circles are matching")
        elif((distance + Circle1.rad) < Circle2.rad):
            print("Circle one is inside circle two")
        elif((distance + Circle2.rad) < Circle1.rad):
            print("Circle two is inside circle one")
        else:
            print("The circles are intersecting")
            
    else:
        print("The circles are touching")



Circle1 = Circle(2, 4, 3)
Circle2 = Circle(4, 4, 5)

find_centre_distance(Circle1, Circle2)