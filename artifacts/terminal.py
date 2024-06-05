# artifacts/terminal.py

import tkinter as tk
from tkinter import ttk
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

        # Create manual entry
        self.create_manual_entry()

        # Create Run button below the scan dropdown and pass the get_manual_command method
        self.run_button = RunButton(self.right_frame, self.get_manual_command, self.update_output)

        # Create output display
        self.create_output_display()

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
        # Create output display treeview widget
        self.output_label = tk.Label(self.root, text="Output:", font=("Helvetica", 12))
        self.output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.output_tree = ttk.Treeview(self.root, show="headings")
        self.output_tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def get_manual_command(self):
        # Return the manual command
        return self.manual_command_var.get()

    def update_output(self, text):
        # Clear the previous output
        for item in self.output_tree.get_children():
            self.output_tree.delete(item)

        # Clear existing columns
        self.output_tree["columns"] = ()
        
        lines = text.strip().split("\n")

        # Filter out lines containing progress or irrelevant information
        relevant_lines = [line for line in lines if line.strip() and not any(keyword in line for keyword in ["Volatility", "Progress", "Reading Symbol layer", "PDB scanning finished"])]

        # Debug: Print the relevant lines
        print("Relevant lines:", relevant_lines)

        if relevant_lines:
            # Assume the first relevant line contains the headers
            headers = relevant_lines[0].split("\t")  # Split by tab as headers are tab-separated
            self.output_tree["columns"] = headers

            for col in headers:
                self.output_tree.heading(col, text=col, command=lambda c=col: self.sort_by(self.output_tree, c, 0))
                self.output_tree.column(col, anchor="w")

            # Insert the rows of data
            for line in relevant_lines[1:]:
                values = line.split("\t")  # Split by tab as values are tab-separated
                # Debug: Print the values
                print("Values:", values)
                
                if len(values) == len(headers):
                    self.output_tree.insert("", "end", values=values)
                else:
                    # Debug: Print a warning if values don't match headers length
                    print("Warning: Mismatch in header and values length. Values:", values)

    def sort_by(self, tree, col, descending):
        # Get the data to be sorted
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        # Sort the data
        data.sort(reverse=descending)
        for index, item in enumerate(data):
            tree.move(item[1], '', index)
        # Reverse sort next time
        tree.heading(col, command=lambda c=col: self.sort_by(tree, c, int(not descending)))

    def run(self):
        # Start the main event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the main application
    root = tk.Tk()
    app = MainApp(root)
    app.run()
