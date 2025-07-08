# 16. Write a Python function to calculate the area of a circle given its radius.
from math import pi as p
def circleArea(r):
  return  r*r*p

radius=float(input("Enter radius of circle.."))
print(f"Area circle : {circleArea(radius):.2f}")