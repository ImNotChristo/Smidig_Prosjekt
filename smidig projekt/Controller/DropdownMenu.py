import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from tkinter import *

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

class RunButtonFunction:
    def __init__(self, master):
        self.master = master
        self.btn = None
        self.create_button()
    
    def create_button(self):
        self.btn = Button(self.master, text='RUN', command=self.master.destroy)
        self.btn.place(x=250, y=10)

class FinishedImageButton:
    def __init__(self, file_entry):
        self.file_entry = file_entry

    def select_image_file(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("JPEG files", "*.jpeg"),
                ("GIF files", "*.gif"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*"),
                ("Raw files", "*.raw")
            ]
        )

        if file_path:
            # Display the selected file path in a message box
            messagebox.showinfo("Selected Image File", f"Selected file: {file_path}")
            # Update the file entry field
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
