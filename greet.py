# Ask the user for their name and age, and then print out a greeting message with their name and age.


name=input("Enter your name. ")
while True:
  try:
    age=int(input("Enter your age!"))
    if age>0:
      break
  except:
    print("Age must be an integer.")
print("Hello!")
print(f"\t{name}, And you are {age}.")