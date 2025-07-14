# Create a list of numbers on given n and then  create a new list with only the even numbers.
n=int(input("Enter n: "))
li=list(range(n+1))
# way first
evens=list(filter(lambda x:x%2==0,li))
print(f"1_List :{evens}")
evens=[x for x in li if x%2==0]
print(f"2_List :{evens}")