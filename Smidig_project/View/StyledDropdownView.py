import tkinter as tk
from tkinter import ttk
from Controller.DropDownMenuController import SearchableCombobox

class StyledDropdown:
    def __init__(self, master, options):
        self.master = master
        self.options = options
        self.create_widgets()

    def create_widgets(self):
        self.selected_option = tk.StringVar(value="")

        self.label = ttk.Label(self.master, text="Scan:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="w")

        self.combobox = SearchableCombobox(self.master, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, pady=10, sticky="w")

        self.show_selected_button = ttk.Button(self.master, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="w")

    def show_selected(self):
        print("Selected item:", self.selected_option.get())
