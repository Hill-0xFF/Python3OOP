class Point:
  def __init__(self, x: int = 0, y: int = 0) -> int:
    self.move(x, y)

  def move(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def reset(self) -> None:
    self.move(0, 0)

pnt1 = Point(1, 3)
print(pnt1.x, pnt1.y)

pnt2 = Point()
print(pnt2.x, pnt2.y)