from notesentry import NotesEntry

class NotesView:
    '''
    Wrapper for lotus.domino.View class
    '''

    def __init__(self,view):
        self.view=view
        self.known_entries = []

    def _entrycollection_to_list(self,collection):
        new_list=[]
        entry = collection.getFirstEntry()
        while entry:
            new_list.append(NotesEntry(entry))
            entry = collection.getNextEntry()
        return new_list

    def get_entries(self):
        return self._entrycollection_to_list(self.view.getAllEntries())

    def get_unread_entries(self):
        return self._entrycollection_to_list(self.view.getAllUnreadEntries())

    def get_new_entries(self):
        '''
        Checks new unread entry IDs against previously known list of IDs.
        If an entry is marked as unread it will be picked up again as a new unread entry.
        TODO: not sure if I want to "fix" this
        '''
        unread_entries = self.get_unread_entries()
        new_known_entries = []
        new_entries = []
        for entry in unread_entries:
            if entry.ID not in self.known_entries:
                new_entries.append(entry.ID)
            new_known_entries.append(entry.ID)
        self.known_entries = new_known_entries
        return new_entries


            


