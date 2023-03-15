import math

class Point:
  def move(self, x: int, y: int):
    self.x = x
    self.y = y

  def reset(self):
    self.x = 0
    self.y = 0

  def calculateDistance(self, otherPoint):
    return math.sqrt(
      (self.x - otherPoint.x) ** 2 + 
      (self.y - otherPoint.y) ** 2
    )

pnt1 = Point()
pnt2 = Point()

pnt1.reset()
pnt2.move(5, 0)
print(pnt2.calculateDistance(pnt1))

assert(pnt2.calculateDistance(pnt1) == 
  pnt1.calculateDistance(pnt2))

pnt1.move(3,4)
print (pnt1.calculateDistance(pnt2))
print(pnt2.calculateDistance(pnt1))

print("Px: {} Py: {}".format(pnt1.x, pnt1.y))