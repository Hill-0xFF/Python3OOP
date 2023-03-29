import datetime

# Store the next available ID for all new notes
last_id = 0

class Note:
  '''
  Represent a note in a notebook.
  Match against a string in searches and
  store tags for each note
  '''

  def __init__(self, memo, tags=''):
    '''
    Initialize a note with memo and optional 
    space-separated tags. Automatically set
    the note's creation date and id
    '''
    self.memo = memo
    self.tags = tags
    self.creationDate = datetime.date.today()
    global last_id
    last_id += 1
    self.id = last_id

  def match(self, filter):
    '''
    Determine if this note matches the filter text.
    Return True if it matches, False otherwise.
    Search is case sensitive and matches both text
    and tags.
    '''
    return filter in self.memo or filter in self.tags


class Notebook:
  '''
  Represent a collection of notes that can be tagged,
  modified and searched.
  '''

  def __init__(self):
    '''
    Initialize a notebook with an empty list
    '''
    self.notes = []

  def newNote(self, memo, tags=''):
    '''
    Create a new note
    '''
    self.notes.append(Note(memo, tags))

  def modifyMemo(self, note_id, memo):
    '''
    Find the note with given id and
    change its contents.
    '''
    for note in self.notes:
      if note.id == note_id:
        note.memo = memo
        break

  def modifyTags(self, note_id, tags):
    '''
    Find the note with given id and
    modify its contents.
    '''
    for note in self.notes:
      if note.id == note_id:
        note.tags = tags
        break

  def searchNote(self, filter):
    '''
    Find all notes that match the given filter
    '''
    return [note for note in self.notes if note.match(filter)]

  def _findNote(self, note_id):
    '''
    Better way to find notes, isolating this responsability
    to it's own function.
    '''
    for note in self.notes:
      if str(note.id) == str(note_id):
        return note
    return None

  def new_modifyMemo(self, note_id, memo):
    '''
    Just modify the memo contents.
    Still needs to search, but using a proper function
    for this job.
    '''
    self._findNote(note_id).memo = memo
