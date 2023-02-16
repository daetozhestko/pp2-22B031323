import math
global pi 
pi=math.pi
def area_polygon(s,n):
    angle=float(pi/n)
    apothem=float(s/(2*math.tan(angle)))
    area=int((apothem*s*n)/2)
    print(area)
s=float(input())
n=float(input())
area_polygon(s,n)