"""
 Binary Search Program....
 Date 05-04-025 """
# Binary Search Function
def binSearch(val,listt):
    listt=list(set(listt))
    beg=0
    mid=len(listt)//2
    end=len(listt)-1
    # search Algorithm
    while beg<=end:
        mid=((end+beg)//2)
        if(val==listt[mid]):
            return True
        elif val>listt[mid]:
            beg=mid+1
        else:
            end=mid-1
    else:
        return False
    

# Size of list in position
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


# Taking elements of list
def getListEle(size):
    listt=[]
    iter=0
    print("Please enter values integer type")
    while iter<size:
        try:
            val=int(input(f"Enter {iter+1} value: "))
            listt.append(val)
            listt.sort(key=int)
            iter+=1
        except:
            print("Only integer type please..")
    return listt

def __main__():
        listSize=getSize()
        listt=getListEle(listSize)
        print(listt)
        while True:
            try:
                searchVal=int(input("Enter val  you want to search in list."))
                break
            except:
                print("Integer type value please..")
            
        searched=binSearch(searchVal,listt)

        if searched:
            print(f"{searchVal} found at index : {listt.index(searchVal)}")
        else:
            print(f"{searchVal} not found in entered list.")

# Calling main function
if __name__=="__main__":
    __main__()