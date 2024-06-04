import tkinter as tk
from tkinter import ttk
from Controller.DropDownMenuController import SearchableCombobox

class StyledDropdown:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.create_widgets()

    def create_widgets(self):
        # Create dropdown and associated widgets
        self.selected_option = tk.StringVar(value="")

        self.label = ttk.Label(self.master, text="Command:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.combobox = SearchableCombobox(self.master, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, pady=10, sticky="w")

    def show_selected(self):
        # Show the selected item in the dropdown menu
        print("Selected item:", self.selected_option.get())
