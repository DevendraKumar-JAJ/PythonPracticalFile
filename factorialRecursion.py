# Write a Python program to find the factorial of a given number using recursion.
import functools
def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)

while True:
  n= int(input("Enter n: "))
  if n>0:
    # through function call
    print(fact(n))
    li=list(range(1,n+1))
    break

# through reduce function
fac=functools.reduce(lambda x,y:x*y,li)
print(fac)


