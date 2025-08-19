#Solution-1

base = float(input("Please enter the base of number: "))
high = float(input("Please enter the high base of number: "))

area = base * high

print("The area of your number is " + str(area))


#Solution-2

import math

a = float(input("Enter the length of side a:"))
b = float(input("Enter the length of side b:"))
c = float(input("Enter the length of side c:"))

s = (a+b+c)/2

area = math.sqrt(a*a + b*b + c*c)

print("the area of the triangle is ", area)

#Solution-3

height = float(input("Enter your height in triangle: "))
base = float(input("Enter your base feet in triangle: "))

area = (base * height) / 2

print("The area of the triangle is", area)

