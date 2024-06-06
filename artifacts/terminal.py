# artifacts/terminal.py

import tkinter as tk
from View.StyledDropdownView import StyledDropdown
from View.StyledImageButtonView import StyledImageButton
from View.RunButtonView import RunButton

class MainApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Artifacts vol.py (GUI)")
        self.root.geometry("1440x600")

        # Create main frames
        self.create_frames()

        # Create file selection on the left
        self.styled_image_button = StyledImageButton(self.left_frame)

        # Manual command variable
        self.manual_command_var = tk.StringVar()

        # Create scan dropdown on the right
        options = [
            "windows.info", "windows.pslist", "windows.psscan", "windows.pstree", "windows.dumpfiles", 
            "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", 
            "windows.netstat", "windows.registry.printkey", "windows.filescan", "windows.dumpfiles"
        ]
        sorted_options = sorted(options)
        self.dropdown = StyledDropdown(self.middle_frame, sorted_options, self.manual_command_var, self.styled_image_button.get_file_path)

<<<<<<< Updated upstream
        # Create manual entry
        self.create_manual_entry()

        # Create Run button below the scan dropdown and pass the get_manual_command method
        self.run_button = RunButton(self.right_frame, self.get_manual_command, self.update_output)

        # Create output display
        self.create_output_display()
=======
        # Create Run button below the scan dropdown and pass the get_selected_option method
        self.run_button = RunButton(self.right_frame, self.dropdown.get_selected_option, self.styled_image_button.get_file_path)
>>>>>>> Stashed changes

    def create_frames(self):
        # Create frames for organizing layout
        self.left_frame = tk.Frame(self.root, width=300, height=150)
        self.left_frame.grid(row=0, column=0, padx=10, pady=13, sticky="n")

        self.middle_frame = tk.Frame(self.root, width=300, height=150)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.right_frame = tk.Frame(self.root, width=300, height=150)
        self.right_frame.grid(row=1, column=2, padx=10, pady=10, sticky="n")

    def create_manual_entry(self):
        # Create manual command entry
        self.manual_label = tk.Label(self.middle_frame, text="Manual Command:", font=("Helvetica", 12))
        self.manual_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.manual_entry = tk.Entry(self.middle_frame, textvariable=self.manual_command_var, width=80)
        self.manual_entry.grid(row=1, column=1, pady=10, sticky="w")

    def create_output_display(self):
        # Create output display text widget
        self.output_label = tk.Label(self.root, text="Output:", font=("Helvetica", 12))
        self.output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.output_text = tk.Text(self.root, wrap=tk.WORD, width=100, height=20)
        self.output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def get_manual_command(self):
        # Return the manual command
        return self.manual_command_var.get()

    def update_output(self, text):
        # Update the output display with new text
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)

    def run(self):
        # Start the main event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the main application
    root = tk.Tk()
    app = MainApp(root)
    app.run()

