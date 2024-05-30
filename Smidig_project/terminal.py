import tkinter as tk
from View.StyledDropdownView import StyledDropdown
from View.StyledImageButtonView import StyledImageButton
from View.RunButtonView import RunButton

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Volatility 3 GUI")
        self.root.geometry("800x600")

        options = [
            "windows.pslist", "windows.psscan", "windows.pstree", "windows.cmdline",
            "windows.services", "windows.registry", "windows.filescan", "windows.malware",
            "windows.network", "windows.memory", "windows.disk", "windows.eventlog",
            "windows.prefetch", "windows.timeline", "windows.locks", "windows.hooks",
            "windows.sysinfo", "windows.drivers", "windows.pipes", "windows.sockets"
        ]
        
        sorted_options = sorted(options)
        dropdown = StyledDropdown(self.root, sorted_options)
        
        run_button = RunButton(self.root)
        styled_image_button = StyledImageButton(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.run()
