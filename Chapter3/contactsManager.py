class Contact:
  allContacts: list = []
  def __init__(self, name: str, email: str):
    self.name = name
    self.email = email
    Contact.allContacts.append(self)

class Supplier(Contact):
  def order(self, order):
    print("If this were a real system we would send"
    "'{}' order to '{}'".format(order, self.name))