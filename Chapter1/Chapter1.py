import time 

class Customer:
  def __init__(self, firstName: str, lastName: str) -> None:
    self.firstName = firstName
    self.lastName = lastName

class Barrel:
  def __init__(self, size: int, apples: list):
    self.size = size
    self.apples = apples

  def __del__(self):
    print("Object from class {} deleted!".format(self.__class__.__name__))

class Basket:
  def __init__(self, location: str, oranges: list) -> None:
    self.location = location
    self.oranges = oranges

  def sell(self, customer: Customer) -> None:
    pass

  def discard(self) -> None:
    pass

class Orange:
  def __init__(self, weight: float, orchard: str, date_picked: time.time() , basket: Basket) -> None:
    self.weight = weight
    self.orchard = orchard
    self.date_picked = date_picked
    self.basket = basket

  def pick(self, basket: Basket) -> None:
    pass

  def squeeze(self) -> int:
    pass

class Apple:
  def __init__(self, color: str, weight: float, barrel: Barrel) -> None:
    self.color = color
    self.weight = weight
    self.barrel = barrel

barrel = Barrel(4, ['ruiva', 'loira'])
print(barrel)

del barrel
