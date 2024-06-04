import tkinter as tk
from tkinter import ttk

class ManualCommandField:
    def __init__(self, master): 
        self.master = master 
        self.create_manual_command_field()

    def create_manual_command_field(self):
        self.entry = ttk.Entry(self.master)
    
    #Returning widget from view 
    def get_entry(self):    
        return self.entry
    