"""Write a Python program to implement a stack using a list. The program should have functions to push/push, pop/pop, showStack, and peek of stack elements from the stack using class."""
# Date : 07-04-025
# CodeBy : Devendra Kumar

from sys import exit 
# to get a valid stack size from user
def stackSize():
  while True:
    try:
      stackSize=int(input("Enter size of stack : "))
      if stackSize>0:
        break
      else:
        print("Value must be a natural number.")
    except ValueError:
      print("Value must be a natural number.")
  return stackSize

# to get user choice on stack operations
def opChoice():
  print("\n1_push, 2_pop, 3_Peek, 4_ShowStack, 5_Exit")
  while True:
    try:
      choice=int(input("Enter your  choice : "))
      break
    except:
      print("Enter a natural number.")
  return choice 

#  a stak tamplate with inbuilt  push,  pop, showpeek, showstack operations methods
class Stack:
  def __init__(self):
    self.stack=[]
    self.top=-1
    self.n=stackSize()
    
  # push/push function 
  def push(self):
    if self.top>self.n-2:
      print("\nStack is overflow")
    else:
      self.top+=1
      ele=input("\nEnter element : ")
      self.stack.append(ele)
      
  # pop/pop function 
  def pop(self):
    if self.top<0:
      print("\nStack underflow.")
    else:
      self.top-=1
      print(f"\nEle poped: {self.stack.pop()}")
      
  #show peek of stack function
  def showPeek(self):
    if len(self.stack)<=0:
      print(f"\nPeekIdx: {len(self.stack)-1}, Stack is empty")
    else:
      print(f"\nPeekIdx: {len(self.stack)-1}, PeekEle: {self.stack[-1]}")
      
  #show all stack elements
  def showStack(self):
    print(f"\nStack is : {self.stack}")
    
    
def main():
  stack1=Stack()
  while True:
    ch=opChoice()
    match ch:
      case 1:
        stack1.push()
      case 2:
        stack1.pop()
      case 3:
        stack1.showPeek()
      case 4:
        stack1.showStack()
      case 5:
        exit()
      case _:
        print("wrong operation choice.")

if __name__=="__main__":
  main()