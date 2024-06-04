# artifacts/View/RunButtonView.py

import tkinter as tk
from Controller.RunButtonController import RunButtonFunction
import subprocess

class RunButton:
    def __init__(self, master, get_manual_command):
        self.master = master
        self.get_manual_command = get_manual_command
        self.create_button()

    def create_button(self):
        # Create Run button
        self.btn = RunButtonFunction(self.master, self.run_command).btn
        self.btn.grid(row=0, column=0, pady=10, sticky="w")

    def run_command(self):
        # Fetch the manual command
        manual_command = self.get_manual_command()
        print(f"Run button clicked. Manual command: {manual_command}")
        # Add functionality to execute the manual command using Volatility
        self.execute_volatility_command(manual_command)

    def execute_volatility_command(self, command):
        if not command:
            print("Command not specified.")
            return
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        except Exception as e:
            print(f"Error running Volatility command: {e}")
