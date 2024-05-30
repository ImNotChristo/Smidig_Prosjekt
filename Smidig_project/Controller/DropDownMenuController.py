import tkinter as tk
from tkinter import ttk

class SearchableCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # List of all possible completion entries
        self._completion_list = []
        # List of all possible completion entries
        self._hits = []
        # Position of the cursor in the combobox
        self.position = 0
        # Bind key release event to handle_keyrelease method
        self.bind('<KeyRelease>', self.handle_keyrelease)
        # Bind mouse click event to show all options
        self.bind('<Button-1>', self.show_all_options)
        # Bind focus in event to on_focus_in method
        self.bind('<FocusIn>', self.on_focus_in)

    def set_completion_list(self, completion_list):
        # Set and sort the completion list
        self._completion_list = sorted(completion_list)
        self['values'] = self._completion_list

    def autocomplete(self):
        """
            Autocomplete based on the user's input.
        """
        # Get the current input from the combobox and convert to lowercase
        search_term = self.get().lower()
        # Filter the hits based on the input
        _hits = self.filter_hits(search_term)

        if _hits != self._hits:
            # Update hits if different from previous hits
            self._hits = _hits

        if _hits:
            # Update the combobox values with hits and show the dropdown
            self['values'] = _hits
            self.event_generate('<Down>')

    def filter_hits(self, search_term):
        """
            Filter the completion list based on the search term.
        """
        # Return items that contain the search term
        hits = [item for item in self._completion_list if search_term in item.lower()]
        return hits

    def handle_keyrelease(self, event):
        """
            Handle key release event for autocomplete.
        """
        # Ignore certain keys for autocomplete
        if event.keysym in ('Left', 'Right', 'Up', 'Down', 'BackSpace', 'Delete'):
            return
        # Update the position of the cursor
        self.position = len(self.get())
        # Perform autocomplete
        self.autocomplete()
        # Maintain the cursor position
        self.icursor(self.position)
        # Keep focus on the combobox
        self.focus()

    def show_all_options(self, event=None):
        """
            Show all options in the dropdown menu.
        """
        # Update the combobox values with the full completion list and show the dropdown
        self['values'] = self._completion_list
        self.event_generate('<Down>')
        self.focus()

    def on_focus_in(self, event):
        # Handle focus in event to maintain cursor position.
        self.icursor(self.position)
