import tkinter as tk
from tkinter import ttk
from Controller.ManualCommandController import ManualCommandField

class ManualCommandFieldStyle:
    def __init__(self, master):
        self.master = master 
        self.create_manual_command_field()

# Styling the input field 
    def create_manual_command_field(self):
        self.label = ttk.Label(self.master, text="Manual", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        manual_command_field = ManualCommandField(self.master)
        self.entry = manual_command_field.get_entry()
        self.entry.grid(row=0, column=1, pady=10, sticky="w")

        # Formatting the input field 
        self.command_entry = tk.Entry(self.master, width=60)
        self.command_entry.grid(row=0, column=1)


