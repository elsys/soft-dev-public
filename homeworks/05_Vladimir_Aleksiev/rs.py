import math

def circle(c1,r1,c2,r2):
    
    x=math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2) - (r2 + r1)
    if(x == 0):
        print("tuching")
        return 

    if((c2 == c1)and(r1==r2)):
        print("matching")
        return
    
    if(r1>r2):
        d= math.sqrt( (c2[0]-c1[0])**2 + (c2[1]-c1[1])**2 )
        if(r1> d):
            print("circle1 is containing circle2")
            return
    else:
        e= math.sqrt( (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 )
        if(r2>e):
            print("circle2 is containing circle1")
            return

    if(x < 0):
        print("intercepting")
        return

    if(x > 0):
        print("NO Common")
        print("the distance in px = ", x)
        return



x=2
y=0
x1=2
y2=0
cx1=(x,y)
cx2=(x1,y2)
rx1=2
rx2=1
circle(cx1,rx1,cx2,rx2)