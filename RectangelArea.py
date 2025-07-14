# Write a Python program to calculate the area of a rectangle given its length and width.

while True:
  try:
    width=float(input("Enter rectangle width. "))
    length=float(input("Enter rectangle length. "))
    if width>0 and length>0:
      break
  except:
    print("Length and width must be number type. ")

print(f"Area of Rectangle.\n : Length = {length}, Width = {width}.\n Area = {length*width}")