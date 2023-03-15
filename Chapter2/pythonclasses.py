class Point:
  def reset(self):
    self.x = 0
    self.y = 0

pnt1 = Point()
pnt1.reset()
print("Px: {} Py: {}".format(pnt1.x, pnt1.y))