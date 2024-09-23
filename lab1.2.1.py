import math as m
a=int(input("enter the side side1:"))
b=int(input("enter the side side2:"))
c=int(input("enter the side side3:"))
s=(a+b+c)/2
area=m.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)