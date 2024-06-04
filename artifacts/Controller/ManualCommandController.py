import tkinter as tk
from tkinter import ttk

class ManualCommandField:
   def __init__(self, master): 
    self.master = master 
    self.create_manual_command_field()

#Creates text entry field and places (50,50) in the window
   def create_manual_command_field(self):
    self.entry = ttk.Entry(self.master)

# Place it within the window.
    self.entry.place(x=50, y=50) 

