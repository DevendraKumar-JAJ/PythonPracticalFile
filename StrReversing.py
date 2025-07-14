# Write a Python program to reverse a given string.
# way first
str =input("Enter your string.")
print(str[::-1])

# way second
revStr=''
for charr in str:
  revStr=charr+revStr
print(revStr)