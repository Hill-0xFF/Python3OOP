class ContactList (list):
  def search(self, name):
    '''
    Return all contacts that contain the search value
    in their name.
    '''
    matching_contacts = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts

class Contact:
  # allContacts: list = []
  allContacts = ContactList()
  def __init__(self, name: str, email: str):
    self.name = name
    self.email = email
    Contact.allContacts.append(self)

# class Friend(Contact):
#   def __init__(self, name, email, phone):
#     self.name = name
#     self.email = email
#     self.phone = phone
# Not the best way to create a class inherited from Contact class

class Friend(Contact):
  def __init__(self, name, email, phone):
    super().__init__(name, email)
    self.phone = phone

class Supplier(Contact):
  def order(self, order):
    print("If this were a real system we would send"
    "'{}' order to '{}'".format(order, self.name))