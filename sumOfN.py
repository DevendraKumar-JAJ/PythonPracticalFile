# Create a list of numbers from 1 to 10 and print out the sum of all the numbers in the list.

import functools
n=int(input("Enter n  : "))

allNums=range(1,n+1)
sum=0

# first way
for num in allNums:
  sum+=num
print(f"1_Sum of 1 to {n} = {sum}")

# second way
sum2=(n*(n+1))//2
print(f"2_Sum of 1 to {n} = {sum2}")

sum3=functools.reduce(lambda x,y:x+y,allNums)
print(sum3)