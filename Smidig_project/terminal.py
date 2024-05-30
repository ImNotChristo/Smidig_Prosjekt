import tkinter as tk
from View.StyledDropdownView import StyledDropdown
from View.StyledImageButtonView import StyledImageButton
from View.RunButtonView import RunButton

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Volatility 3 GUI")
        self.root.geometry("800x600")

        # Create main frames
        self.create_frames()

        # Create file selection on the left
        self.styled_image_button = StyledImageButton(self.left_frame)

        # Create scan dropdown on the right
        options = [
            "windows.info", "windows.pslist", "windows.psscan", "windows.pstree", "windows.dumpfiles", 
            "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", 
            "windows.netstat", "windows.registry.printkey", "windows.filescan", "windows.dumpfiles"
        ]
        sorted_options = sorted(options)
        self.dropdown = StyledDropdown(self.right_frame, sorted_options)

        # Create Run button below the scan dropdown
        self.run_button = RunButton(self.right_frame)

    def create_frames(self):
        self.left_frame = tk.Frame(self.root, width=300, height=150)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        self.right_frame = tk.Frame(self.root, width=300, height=150)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.run()
