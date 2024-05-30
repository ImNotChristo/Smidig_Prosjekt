import tkinter as tk
from Controller.RunButtonController import RunButtonFunction

class RunButton:
    def __init__(self, master):
        self.master = master
        self.create_button()

    def create_button(self):
        self.btn = RunButtonFunction(self.master, self.run_command).btn
        self.btn.grid(row=2, column=0, pady=10, sticky="w")

    def run_command(self):
        print("Run button clicked")
        # Add your functionality here
