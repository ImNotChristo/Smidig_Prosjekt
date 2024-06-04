import tkinter as tk
import tkinter as ttk

from Controller.ManualCommandController import ManualCommandField

class ManualCommandFieldStyle:
    def __init__(self, master):
        self.master = master 
        

    def create_manual_command_field(self):
        self.entry = ManualCommandField(self.master)
        self.entry.grid(row=0, column=0, pady=10, sticky="w")

        self.label = ttk.Label(self.master, text="Manual:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
  
  