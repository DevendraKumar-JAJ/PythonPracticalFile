# Create a class with a method to calculate the area of a rectangle given its length and width.\
class recArea:
  def __init__(self,length,width):
    self.a=length*width
  def area(self):
    print('Area of rectangle : ',self.a)


rectangle=recArea(13,5)
rectangle.area()
rectangle=recArea(27,3)
rectangle.area()