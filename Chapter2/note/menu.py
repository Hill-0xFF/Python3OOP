import sys

from notebook import Note, Notebook

class Menu:
  '''
  Shows a menu and do whatever the user need to do.
  '''
  def __init__(self):
    self.notebook = Notebook()
    self.options = {
      "1": self.showNotes,
      "2": self.searchNote,
      "3": self.addNote,
      "4": self.modifyNote,
      "5": self.Quit
    }

  def displayMenu(self):
    print("\t\t\tNOTEBOOK MENU\n")
    print("""
    1). Show all Notes
    2). Search Notes
    3). Add Note
    4). Modify Note
    5). Exit Program
    """)

  def run(self):
    '''
    Display the menu and respond to options.
    '''
    while True:
      self.displayMenu()
      choices = input("Choose an option: ")
      action = self.options.get(choices)
      if action:
        action()

      else:
        print("{} is not an option".format(choices))

  def showNotes(self, notes= None):
    if not notes:
      notes = self.notebook.notes

    for note in notes:
      print ("{0}: {1}\n {2}".format(note.id, note.tags, note.memo))

  def searchNote(self):
    filter = input("Search for: ")
    notes = self.notebook.searchNote(filter)
    self.showNotes(notes)


  def addNote(self):
    memo = input("Enter a memo: ")
    self.notebook.newNote(memo)
    print("\nYour note has been added.")

  def modifyNote(self):
    id = input ("Enter a note ID: ")
    memo = input ("Enter a memo: ")
    tags = input("Enter tags: ")
    if memo:
      # self.notebook.modifyMemo(id, memo)
      self.notebook.new_modifyMemo(id, memo)
    
    if tags: 
      # self.notebook.modifyTags(id, tags)
      self.notebook.new_modifyTags(id, tags)

  def Quit(self):
    print("\n\t\t\tThanks for using Notebook™")
    sys.exit(0)

if __name__ == "__main__":
  Menu().run()