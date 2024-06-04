import tkinter as tk
from View.StyledDropdownView import StyledDropdown
from View.StyledImageButtonView import StyledImageButton
from View.RunButtonView import RunButton 
from View.OutputFieldView import OutputField

class MainApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Artifacts vol.py (GUI)")
        self.root.geometry("800x600")
        # self.root.configure(bg='white')

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
        self.dropdown = StyledDropdown(self.middle_frame, sorted_options)

        # Create Run button below the scan dropdown
        self.run_button = RunButton(self.right_frame)

        # Create Output field
        self.create_ouputfield = OutputField(self.output_frame)

    def create_frames(self):
        # Create frames for organizing layout
        self.left_frame = tk.Frame(self.root, width=300, height=150)
        self.left_frame.grid(row=0, column=0, padx=10, pady=13, sticky="n")

        self.middle_frame = tk.Frame(self.root, width=300, height=150)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.right_frame = tk.Frame(self.root, width=300, height=150)
        self.right_frame.grid(row=1, column=2, padx=10, pady=10, sticky="n")

        # LA TIL
        self.output_frame = tk.Frame(self.root, width=60, height=50)
        self.output_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")

    def run(self):
        # Start the main event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create and run the main application
    root = tk.Tk()
    app = MainApp(root)
    app.run()

