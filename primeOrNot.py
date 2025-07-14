#  Write a Python program to check if a given number is prime or not.
from math import sqrt as s
import sys
num=int(input("Enter number to check."))
if num<=1:
  print("This is not prime number..")
  sys.exit()
  
to=int(s(num))
divCount=0

for iter in range(2,to+1):
  if(num%iter==0):
    divCount+=1
    break
  
if(divCount==0):
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number.")
  