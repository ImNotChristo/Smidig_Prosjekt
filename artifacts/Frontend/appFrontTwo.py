import tkinter as tk
from tkinter import ttk, filedialog
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
        self.file_button = tk.Button(top_frame, text="Browse", command=self.browse_file)
        self.file_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Platform Selection
        tk.Label(top_frame, text="Platform:").grid(row=0, column=3, padx=5, pady=5)
        self.platform_combobox = ttk.Combobox(top_frame, values=["Windows", "Linux", "Mac"])
        self.platform_combobox.grid(row=0, column=4, padx=5, pady=5)
        self.platform_combobox.bind("<<ComboboxSelected>>", self.update_command_options)
        
        # Command Selection
        tk.Label(top_frame, text="Command:").grid(row=0, column=5, padx=5, pady=5)
        self.command_combobox = ttk.Combobox(top_frame)
        self.command_combobox.grid(row=0, column=6, padx=5, pady=5)
        self.command_combobox.bind("<<ComboboxSelected>>", self.update_manual_entry)
        
        # Manual Command Entry
        tk.Label(top_frame, text="Manual:").grid(row=1, column=0, padx=5, pady=5)
        self.manual_entry = tk.Entry(top_frame, width=80)
        self.manual_entry.grid(row=1, column=1, columnspan=5, padx=5, pady=5)
        
        # Scan Button
        self.scan_button = tk.Button(top_frame, text="Scan", command=self.scan_file)
        self.scan_button.grid(row=0, column=7, rowspan=2, padx=5, pady=5, ipadx=10, ipady=5)
        
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
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Mem files", "*.mem"), ("Raw files", "*.raw")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
        
    def scan_file(self):
        file_path = self.file_entry.get()
        platform = self.platform_combobox.get().lower()
        command = self.command_combobox.get()
        
        if not file_path or not platform or not command:
            self.status.set("Status: Please fill all the fields")
            return
        
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
            
    def update_command_options(self, event):
        platform = self.platform_combobox.get().lower()
        commands = {
            "windows": ["windows.pslist", "windows.info", "windows.psscan", "windows.pstree", "windows.dumpfiles", "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", "windows.netstat", "windows.registry.printkey", "windows.filescan"],
            "linux": ["linux.pslist", "linux.info", "linux.psscan", "linux.pstree", "linux.dumpfiles", "linux.memmap", "linux.handles", "linux.dlllist", "linux.cmdline", "linux.netscan", "linux.netstat", "linux.registry.printkey", "linux.filescan"],
            "mac": ["mac.pslist", "mac.info", "mac.psscan", "mac.pstree", "mac.dumpfiles", "mac.memmap", "mac.handles", "mac.dlllist", "mac.cmdline", "mac.netscan", "mac.netstat", "mac.registry.printkey", "mac.filescan"]
        }
        
        self.command_combobox['values'] = commands.get(platform, [])
        self.command_combobox.set('')
        self.manual_entry.delete(0, tk.END)
        
    def update_manual_entry(self, event):
        command = self.command_combobox.get()
        file_path = self.file_entry.get() or "<file_path>"
        platform = self.platform_combobox.get().lower() or "<platform>"
        
        syntax = f"python vol.py -f {file_path} {command}"
        if command in ['windows.dumpfiles', 'windows.memmap', 'windows.handles', 'windows.dlllist', 'linux.dumpfiles', 'linux.memmap', 'linux.handles', 'linux.dlllist', 'mac.dumpfiles', 'mac.memmap', 'mac.handles', 'mac.dlllist']:
            syntax += " --pid <PID>"
        elif command in ['windows.vadyarascan', 'linux.vadyarascan', 'mac.vadyarascan']:
            syntax += " --yara-rules <rules>"
        
        self.manual_entry.delete(0, tk.END)
        self.manual_entry.insert(0, syntax)
            
    def update_table(self, output):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        lines = output.strip().split("\n")
        for line in lines[1:]:  # Skip the header line
            self.tree.insert("", tk.END, values=line.split())

if __name__ == "__main__":
    app = Application()
    app.mainloop()
