import tkinter as tk
from Controller.ManualCommandController import ManualCommandField

class ManualCommandFieldStyle:
    def __init__(self, master):
        self.master = master 
        

    def create_manual_command_field(self):
        self.entry = ManualCommandField(self.master)
        self.entry.grid(row=0, column=0, pady=10, sticky="w")

  
  