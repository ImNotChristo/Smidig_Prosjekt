import tkinter as tk
from tkinter import ttk
from View.StyledDropdownView import StyledDropdown
from View.StyledImageButtonView import StyledImageButton
from View.RunButtonView import RunButton

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Artifacts vol.py (GUI)")
        self.root.geometry("1440x600")

        self.create_frames()
        self.styled_image_button = StyledImageButton(self.left_frame)
        self.manual_command_var = tk.StringVar()

        options = [
            "windows.info", "windows.pslist", "windows.psscan", "windows.pstree", "windows.dumpfiles", 
            "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", 
            "windows.netstat", "windows.registry.printkey", "windows.filescan", "windows.dumpfiles"
        ]
        sorted_options = sorted(options)
        self.dropdown = StyledDropdown(self.middle_frame, sorted_options, self.manual_command_var, self.styled_image_button.get_file_path)

        self.create_manual_entry()
        self.run_button = RunButton(self.right_frame, self.get_manual_command, self.update_output)
        self.create_output_display()

    def create_frames(self):
        self.left_frame = tk.Frame(self.root, width=300, height=150)
        self.left_frame.grid(row=0, column=0, padx=10, pady=13, sticky="n")

        self.middle_frame = tk.Frame(self.root, width=300, height=150)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.right_frame = tk.Frame(self.root, width=300, height=150)
        self.right_frame.grid(row=1, column=2, padx=10, pady=10, sticky="n")

    def create_manual_entry(self):
        self.manual_label = tk.Label(self.middle_frame, text="Manual Command:", font=("Helvetica", 12))
        self.manual_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.manual_entry = tk.Entry(self.middle_frame, textvariable=self.manual_command_var, width=80)
        self.manual_entry.grid(row=1, column=1, pady=10, sticky="w")

    def create_output_display(self):
        self.output_label = tk.Label(self.root, text="Output:", font=("Helvetica", 12))
        self.output_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.output_tree = ttk.Treeview(self.root, show="headings")
        self.output_tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def get_manual_command(self):
        return self.manual_command_var.get()

    def update_output(self, text):
        for item in self.output_tree.get_children():
            self.output_tree.delete(item)

        self.output_tree["columns"] = ()
        
        lines = text.strip().split("\n")
        relevant_lines = [line for line in lines if line.strip() and not any(keyword in line for keyword in ["Volatility", "Progress", "Reading Symbol layer", "PDB scanning finished"])]

        if relevant_lines:
            headers = relevant_lines[0].split("\t")
            self.output_tree["columns"] = headers

            for col in headers:
                self.output_tree.heading(col, text=col, command=lambda c=col: self.sort_by(self.output_tree, c, 0))
                self.output_tree.column(col, anchor="w")

            for line in relevant_lines[1:]:
                values = line.split("\t")
                if len(values) == len(headers):
                    self.output_tree.insert("", "end", values=values)
                else:
                    print("Warning: Mismatch in header and values length. Values:", values)

    def sort_by(self, tree, col, descending):
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=descending)
        for index, item in enumerate(data):
            tree.move(item[1], '', index)
        tree.heading(col, command=lambda c=col: self.sort_by(tree, c, int(not descending)))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.run()
