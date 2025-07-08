# Write a Python program to check if a given number is even or odd.
n=int(input("Enter number. "))

#first way
[print("1_EvenNumber") if n%2==0 else print("1_OddNumber")]

#Second way
if(n%2==0):
  print("2_EvenNumber")
else:
  print("2_oddNumber")
  
  
# third way
if(n&1==0):
  print("3_EvenNumber")
else:
  print("3_OddNumber")