import tkinter as tk

class RunButtonFunction:
    def __init__(self, master, command):
        self.master = master
        self.command = command
        self.create_button()
    
    def create_button(self):
        self.btn = tk.Button(self.master, text='RUN', command=self.command)
        self.btn.place(x=250, y=10)
