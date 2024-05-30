import tkinter as tk
from Controller.RunButtonController import RunButtonFunction

class RunButton:
    def __init__(self, master):
        self.master = master
        self.btn = RunButtonFunction(self.master, self.run_command).btn

    def run_command(self):
        print("Run button clicked")
        # Add your functionality here
