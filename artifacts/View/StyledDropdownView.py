import tkinter as tk
from tkinter import ttk
from Controller.DropDownMenuController import SearchableCombobox
import os

class StyledDropdown:
    def __init__(self, master, options, manual_command_var, get_file_path, label_text="Scan:"):
        self.master = master
        self.options = options
        self.manual_command_var = manual_command_var
        self.get_file_path = get_file_path
        self.create_widgets(label_text)

    def create_widgets(self, label_text):
        # Create dropdown and associated widgets
        self.selected_option = tk.StringVar(value="")

        self.label = ttk.Label(self.master, text=label_text, font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.combobox = SearchableCombobox(self.master, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, pady=10, sticky="w")
        self.combobox.bind('<<ComboboxSelected>>', self.update_manual_command)

    def get_selected_option(self):
        # Return the selected option
        return self.selected_option.get()

    def update_manual_command(self, event):
        # Update the manual command based on the selected option
        selected_command = self.get_selected_option()
        file_path = self.get_file_path()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        vol_path = os.path.join(script_dir, '..', '..', 'volatility3', 'vol.py')

        if selected_command in ['windows.dumpfiles', 'windows.memmap', 'windows.handles', 'windows.dlllist']:
            manual_command = f'python "{vol_path}" -f "{file_path}" -o "/path/to/dir" {selected_command} --pid <PID>'
        elif selected_command == 'windows.vadyarascan':
            manual_command = f'python "{vol_path}" -f "{file_path}" {selected_command} --yara-rules <string>'
        else:
            manual_command = f'python "{vol_path}" -f "{file_path}" {selected_command}'
        self.manual_command_var.set(manual_command)