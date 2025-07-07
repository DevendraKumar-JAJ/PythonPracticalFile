# 6. Create a dictionary with the names of five countries as keys and their capitals as values, and then print out the capital of a given country.

COC={
  "India":"New Delhi",
  "US":"Washington,D.C.",
  "China":"Beijing",
  "Japan":"Tokyo",
  "UnotedKingdom":"Londan"
}


key=input('Enter country name.')

#Way first
try:
  print(f"Capital of {key} is {COC[key]}.")
except:
  print(f"{key} not in dictionary.")
  
# Way Second...
if key in COC:
  print(f"Capital of {key} is {COC[key]}.")
  
else:
  print(f"{key} not in dictionary.")
