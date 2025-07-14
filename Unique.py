# Find  unique  numbers from a list of numbers and print out.
listNums=[1,2,3,4,5,4,4,1,3]

dic={}
unq=[]

for num in listNums:
  if num in dic:
    dic[num]+=1
  else:
    dic[num]=1

for key in dic:
  if dic[key]<=1:
    unq.append(key)

print(f"Unique numbers in list {unq}")


