# artifacts/View/RunButtonView.py

import tkinter as tk
from Controller.RunButtonController import RunButtonFunction
import subprocess
import os


class RunButton:
    def __init__(self, master, get_command, get_file_path):
        self.master = master
        self.get_command = get_command
        self.get_file_path = get_file_path
        self.create_button()

    def create_button(self):
        # Create Run button
        self.btn = RunButtonFunction(self.master, self.run_command).btn
        self.btn.grid(row=0, column=0, pady=10, sticky="w")

    def run_command(self):
        # Fetch the selected command and file path
        selected_command = self.get_command()
        file_path = self.get_file_path()
        print(f"Run button clicked. Selected command: {selected_command}, File path: {file_path}")
        # Add functionality to execute the selected command using Volatility
        self.execute_volatility_command(selected_command, file_path)

    def execute_volatility_command(self, command, file_path):
        if not file_path or not command:
            print("File path or command not specified.")
            return

        # Construct the Volatility command
        script_dir = os.path.dirname(__file__)
        vol_path = os.path.join(script_dir, '..', '..', 'volatility3', 'vol.py')
        
        vol_command = ['python', vol_path, '-f', file_path]

        # Handle special cases for specific commands
        if command in ['windows.dumpfiles', 'windows.memmap', 'windows.handles', 'windows.dlllist']:
            pid = self.ask_for_pid()
            if not pid:
                print("PID not provided.")
                return
            if command == 'windows.dumpfiles':
                output_dir = self.ask_for_output_dir()
                if not output_dir:
                    print("Output directory not provided.")
                    return
                vol_command.extend(['-o', output_dir, command, '--pid', pid])
            elif command == 'windows.memmap':
                output_dir = self.ask_for_output_dir()
                if not output_dir:
                    print("Output directory not provided.")
                    return
                vol_command.extend(['-o', output_dir, command, '--dump', '--pid', pid])
            else:
                vol_command.extend([command, '--pid', pid])
        elif command == 'windows.vadyarascan':
            yara_rules = self.ask_for_yara_rules()
            if not yara_rules:
                print("YARA rules not provided.")
                return
            vol_command.extend([command, '--yara-rules', yara_rules])
        else:
            vol_command.append(command)
        
        try:
            result = subprocess.run(vol_command, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        except Exception as e:
            print(f"Error running Volatility command: {e}")

    def ask_for_pid(self):
        # Ask user for PID
        pid = tk.simpledialog.askstring("Input", "Please enter PID:")
        return pid

    def ask_for_output_dir(self):
        # Ask user for output directory
        output_dir = tk.filedialog.askdirectory(title="Select Output Directory")
        return output_dir

    def ask_for_yara_rules(self):
        # Ask user for YARA rules
        yara_rules = tk.simpledialog.askstring("Input", "Please enter YARA rules:")
        return yara_rules
