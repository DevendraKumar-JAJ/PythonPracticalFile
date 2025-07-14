# Write a Python program to find the maximum and minimum values in a list of numbers.
def getSize():
    print("Size must be greater than 0.")
    while True:
      try:
          size=int(input("Size of List.. "))
          if size>=1:
            break
      except:
        print("Integer type value..")
    return size


def getListEle(size):
    li=[]
    iter=0
    while iter<size:
      try:
        val=int(input(f"Enter {iter+1} value: "))
        li.append(val)
        li.sort(key=int)
        iter+=1
      except:
        print("Only int type")
    return li
  
  
def __main__():
    size=getSize()
    li=getListEle(size)
    print(f"list:{li}")
    # way first need to sorted list
    maax=li[-1]
    miin=li[0]
    print(f"1_Max: {maax}, Min: {miin}")
    # way second // no need to sorted list
    print(f"2_Max: {max(li)}, Min: {min(li)}")
    
if __name__=="__main__":
  __main__()