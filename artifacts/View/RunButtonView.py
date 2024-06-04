import tkinter as tk
from Controller.RunButtonController import RunButtonFunction

class RunButton:
    def __init__(self, master):
        self.master = master
        self.create_button()

    def create_button(self):
        # Create Run button
        self.btn = RunButtonFunction(self.master, self.run_command).btn
        self.btn.grid(row=0, column=0, pady=10, sticky="w")

    def run_command(self):
        # Define Run button command
        print("Run button clicked")
        # Add your functionality here
