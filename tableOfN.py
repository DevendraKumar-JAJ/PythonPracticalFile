# 12. Ask the user for a number and then print out the multiplication table for that number using a while loop in [2*1=2]  format.

n=int(input('Enter n: '))
iter=1
while iter<=10:
  print(f"{n} * {iter} = {n*iter}")
  iter+=1