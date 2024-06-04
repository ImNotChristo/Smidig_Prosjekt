# artifacts/View/StyledDropdownView.py

import tkinter as tk
from tkinter import ttk
from Controller.DropDownMenuController import SearchableCombobox

class StyledDropdown:
    def __init__(self, master, options, label_text="Scan:"):
        self.master = master
        self.options = options
        self.create_widgets(label_text)

    def create_widgets(self, label_text):
        # Create dropdown and associated widgets
        self.selected_option = tk.StringVar(value="")

        self.label = ttk.Label(self.master, text=label_text, font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.combobox = SearchableCombobox(self.master, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, pady=10, sticky="w")

    def get_selected_option(self):
        # Return the selected option
        return self.selected_option.get()
