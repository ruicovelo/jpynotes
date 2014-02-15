from lotus.domino import *
from lotusnotesentry import LotusNotesEntry

'''
This only works if Lotus Notes is running and for local database files.
As of 12/02/2014 I do not plan on supporting any other setup because I don't need any other setup.
Contributions are welcome of course.

Rui Covelo
'''



class LotusNotes:

    def __init__(self,mail_file_path):
        #TODO: not sure what this is but is necessary
        NotesThread.sinitThread()
        # This only works if Lotus Notes is running - not authentication specified
        self.session = NotesFactory.createSession(None,None,None)
        self.database = self.session.getDatabase(None,mail_file_path,False)

    def _entrycollection_to_list(self,collection):
        new_list=[]
        entry = collection.getFirstEntry()
        while entry:
            new_list.append(LotusNotesEntry(entry))
            entry = collection.getNextEntry()
        return new_list
    
    def _get_inbox(self):
        return self.database.getView('($INBOX)')

    def get_inbox_entries(self):
        ''' Return a list of entries in inbox '''
        inbox = self._get_inbox()
        return self._entrycollection_to_list(inbox.getAllEntries())
        
    def get_unread_inbox_entries(self):
        inbox = self._get_inbox()
        return self._entrycollection_to_list(inbox.getAllUnreadEntries())

        
