import math as m
a=int(input("enter the side side1:"))
b=int(input("enter the side side2:"))
c=int(input("enter the side side3:"))
print("the sides of triangle are:",a,b,c)
angle1=m.degrees(m.acos((a**2+b**2-c**2)/(2*a*b)))
angle2=m.degrees(m.acos((a**2-b**2+c**2)/(2*a*c)))
angle3=m.degrees(m.acos((-a**2+b**2+c**2)/(2*c*b)))
print("the angles of this triangle are:",angle2,angle1,angle3)