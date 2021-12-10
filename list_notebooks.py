#!/usr/bin/env python 
from evernote.api.client import EvernoteClient

from config import EVERNOTE_PERSONAL_TOKEN

    
if __name__ == '__main__':

    client = EvernoteClient(
        token=EVERNOTE_PERSONAL_TOKEN,
        sandbox=False
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
