from lotus.domino import *
from notesentry import NotesEntry
from notesview import NotesView

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


    def get_view(self,view_name):
        return NotesView(self.database.getView(view_name))
    
    def get_inbox(self):
        return self.get_view('($INBOX)')


        
