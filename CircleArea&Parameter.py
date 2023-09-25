import math

class Circle():
  def __init__(self,r):
    self.radius=r
  def area(self):
    return pow(self.radius,2)*math.pi
  def perimeter(self):
    return 2*self.radius*math.pi

Circle1=Circle(2)
print(Circle1.area())
print(Circle1.perimeter())
print("Testing")