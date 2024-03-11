from math import *

#1
 
degree = int(input("Input degree: "))
def toRadian(deg):
    rad = radians(deg)
    return rad
print(f"Output radian: {toRadian(degree)}")

#2

height = int(input("Height: "))
base1, base2 = int(input("Base, first value: ")), int(input("Base, second value: "))
def area(height, base1, base2):
    return (base1 + base2) / 2 * height
print(f"Excepted output: {area(height, base1, base2)}")

#3

sides = int(input("Number of sides: "))
length = int(input("The length of a side: "))

def area(a, n):
    R = sqrt(pow(a, 2) / (2 * (1 - cos(radians(360 / n)))))
    triangle = pow(R, 2) * sin(radians(360 / n)) / 2  
    return triangle * n

print(f"The area of the polygon is: {area(length, sides)}")

#4

base = int(input("Lenght of base: "))
heigth = int(input("Height of parallelogram: "))
def area(base, height):
    return base * height     
print(f"Excepted Output: {area(base, height)}")
    

