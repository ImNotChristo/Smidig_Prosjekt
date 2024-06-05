import tkinter as tk
from tkinter import ttk
import requests

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Artifacts")
        self.geometry("1000x700")
        self.create_widgets()
        
    def create_widgets(self):
        # Top Frame for command input
        top_frame = tk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # File Selection
        tk.Label(top_frame, text="File:").grid(row=0, column=0, padx=5, pady=5)
        self.file_entry = tk.Entry(top_frame, width=30)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.file_entry.insert(0, "C:/Users/evenj/OneDrive/Skrivebord/memdump-001.mem")
        
        # Platform Selection
        tk.Label(top_frame, text="Platform:").grid(row=0, column=2, padx=5, pady=5)
        self.platform_combobox = ttk.Combobox(top_frame, values=["Windows", "Linux"])
        self.platform_combobox.grid(row=0, column=3, padx=5, pady=5)
        self.platform_combobox.set("Windows")
        
        # Command Selection
        tk.Label(top_frame, text="Command:").grid(row=0, column=4, padx=5, pady=5)
        self.command_combobox = ttk.Combobox(top_frame, values=["windows.pslist", "windows.info", "windows.psscan"])
        self.command_combobox.grid(row=0, column=5, padx=5, pady=5)
        self.command_combobox.set("windows.pslist")
        
        # Manual Command Entry
        tk.Label(top_frame, text="Manual:").grid(row=1, column=0, padx=5, pady=5)
        self.manual_entry = tk.Entry(top_frame, width=80)
        self.manual_entry.grid(row=1, column=1, columnspan=5, padx=5, pady=5)
        
        # Scan Button
        self.scan_button = tk.Button(top_frame, text="Scan", command=self.scan_file)
        self.scan_button.grid(row=0, column=6, rowspan=2, padx=5, pady=5, ipadx=10, ipady=5)
        
        # Command Parameter Selection Frame
        param_frame = tk.Frame(self)
        param_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        tk.Label(param_frame, text="Command Parameter", font=('Helvetica', 10, 'bold')).pack(anchor=tk.W)
        
        self.param_vars = {
            "PID": tk.BooleanVar(),
            "PPID": tk.BooleanVar(),
            "ImageFileName": tk.BooleanVar(),
            "Offset(V)": tk.BooleanVar(),
            "Threads": tk.BooleanVar(),
            "SessionId": tk.BooleanVar(),
            "Wow64": tk.BooleanVar(),
            "CreateTime": tk.BooleanVar(),
            "ExitTime": tk.BooleanVar(),
            "File output": tk.BooleanVar()
        }
        
        for param, var in self.param_vars.items():
            tk.Checkbutton(param_frame, text=param, variable=var).pack(anchor=tk.W)
        
        # Main Display Frame
        display_frame = tk.Frame(self)
        display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Progress Bar
        self.progress_bar = ttk.Progressbar(display_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=5)
        
        # Results Table
        columns = ["PID", "PPID", "ImageFileName", "Offset(V)", "Threads", "SessionId", "Wow64", "CreateTime", "ExitTime", "File output"]
        self.tree = ttk.Treeview(display_frame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, stretch=tk.NO, width=100)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Status Bar
        self.status = tk.StringVar()
        self.status.set("Status: Ready")
        tk.Label(self, textvariable=self.status, bd=1, relief=tk.SUNKEN, anchor=tk.W).pack(side=tk.BOTTOM, fill=tk.X)
        
    def scan_file(self):
        file_path = self.file_entry.get()
        platform = self.platform_combobox.get().lower()
        command = self.command_combobox.get()
        
        json_data = {
            "FilePath": file_path,
            "Command": command
        }
        
        self.progress_bar.start()
        self.status.set("Status: Scanning...")
        
        try:
            req = requests.post("http://localhost:6000/api/scan", json=json_data)
            self.progress_bar.stop()
            if req.status_code == 200:
                data = req.json()
                self.update_table(data['output'])
                self.status.set("Status: Scan completed")
            else:
                self.status.set(f"Status: Failed to fetch data - {req.status_code}")
        except requests.exceptions.RequestException as e:
            self.progress_bar.stop()
            self.status.set(f"Status: Error - {e}")
            
    def update_table(self, output):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        lines = output.strip().split("\n")
        for line in lines[1:]:  # Skip the header line
            self.tree.insert("", tk.END, values=line.split())

if __name__ == "__main__":
    app = Application()
    app.mainloop()
