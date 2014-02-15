

class LotusNotesEntry:
    '''
    Wrapper for lotus.domino.local.ViewEntry for easier integratoin with python code
    '''

    def __init__(self,viewentry):
            self.viewentry = viewentry
            self.ID = viewentry.universalID
            self.Subject = viewentry.getDocument().getItemValue('Subject')
            self.From = viewentry.getDocument().getItemValue('From')
            self.Body = viewentry.getDocument().getItemValue('Body')

    def __str__(self):
        return self.ID

