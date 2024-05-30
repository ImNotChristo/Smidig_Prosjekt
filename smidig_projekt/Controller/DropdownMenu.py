import tkinter as tk
from tkinter import ttk

class SearchableCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # storage for our list that we are traversing through
        self._completion_list = []
        self._hits = []
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self.bind('<Button-1>', self.show_all_options)
        self.bind('<FocusIn>', self.on_focus_in)

    # function to take in the list that we want to look through and sort it for the dropdown menu
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self['values'] = self._completion_list

    # takes in the input from user and places it in search_term
    def autocomplete(self):
        search_term = self.get().lower()
        # sends in the input from user into the method that will match it with the commands list
        _hits = self.filter_hits(search_term)

        if _hits != self._hits:
            self._hits = _hits

        if _hits:
            self['values'] = _hits
            self.event_generate('<Down>')  # Open the dropdown


    # Method for searching our input string against the list we are traversing through
    def filter_hits(self, search_term):
        hits = [item for item in self._completion_list if search_term in item.lower()]
        return hits

    # handling keyrelease: if we press any of the left right up ... nothing happens if else .. then activates search

    def handle_keyrelease(self, event):
        if event.keysym in ('Left', 'Right', 'Up', 'Down', 'BackSpace', 'Delete'):
            return
        self.position = len(self.get())
        self.autocomplete()
        self.icursor(self.position)  # Maintain the cursor position
        self.focus()  # Keep focus on the combobox

    #dropdown menu
    def show_all_options(self, event=None):
        self['values'] = self._completion_list
        self.event_generate('<Down>')
        self.focus()

    def on_focus_in(self, event):
        self.icursor(self.position)