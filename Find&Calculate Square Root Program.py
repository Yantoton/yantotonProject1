#solution-1 (Using Exponentiation)
num = 86
num1 = int(input("Enter user number:"))
sr = num**(0.5)
print("the square root of  given number is",sr)

#Solution-2(Using Math Module)
import math
num = int(input("Enter the number:"))
sr = math.sqrt(num)
print("The square root of given number is:",sr)
