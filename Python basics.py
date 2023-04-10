print("I love python")
##python as calculator
print(1+2)
print((3*4)/((2**2)+2))
print(3/4)
import math
print(math.sqrt(144))
print(math.sin(math.pi/2))
print(2+5j)
print(complex(1,2))
print(type(2))
print(type(2.1))
##logic expressions and operations
print( (1 and 0) or (0 and 0))
print((1 and 1) or (0 and 1))
##problems
#1
h=12
b=10
area=0.5*b*h
print(area)
#2
import math
x1=3
y1=4
x2=5
y2=9
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance)
#3
def fac(n):
    if n==1 or n==0:
        return 1
    else: 
        return n*fac(n-1)
print(fac(6))
#4
def leap(year):
    for i in range(1500,2011):
        if i%4==0 and (i%100!=0 or i%400==0):
            output="it is a leap year"
            return output
        else:
            output="not a leap year"
            return output
