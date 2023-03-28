import math

class Point:
  'Representing points in a two-dimensional geometric coordinates'
  def __init__(self, x: int = 0, y: int = 0) -> int:
    '''
    Initialize the position of a new point. The X and Y coordinates can be specified.
    If not specified, it'll set default value, which is 0.
    '''
    self.move(x, y)

  def move(self, x: int, y: int) -> None:
    '''
    Move the point to a new location in a 2D space
    '''
    self.x = x
    self.y = y

  def reset(self) -> None:
    '''
    Sets a new point in a 2D space back to origin: 0, 0
    '''
    self.move(0, 0)

  def calculateDistance(self, otherPoint) -> float:
    '''
    Calculate the distance between two points in a 2D space.
    Uses the Pythagorean Theorem calculate the said distance.
    Return value as float
    '''
    return math.sqrt(
      (self.x - otherPoint.x) ** 2 +
      (self.y - otherPoint.y) ** 2
    )


pnt1 = Point(1, 3)
print(pnt1.x, pnt1.y)

pnt2 = Point()
print(pnt2.x, pnt2.y)
