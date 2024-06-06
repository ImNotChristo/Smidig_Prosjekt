import tkinter as tk
from tkinter import ttk, filedialog
import requests

"""
components.py

This file contains helper functions for creating and managing the GUI components
of the Tkinter application. It includes functions for initializing widgets,
handling file browsing, sending scan requests, and updating the display.
"""

def create_widgets(app):
    """
    Create and initialize the main widgets for the application.
    """
    # Top Frame for command input
    top_frame = tk.Frame(app)
    top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    # File Selection
    tk.Label(top_frame, text="File:").grid(row=0, column=0, padx=5, pady=5)
    app.file_entry = tk.Entry(top_frame, width=30)
    app.file_entry.grid(row=0, column=1, padx=5, pady=5)
    app.file_button = tk.Button(top_frame, text="Browse", command=app.browse_file)
    app.file_button.grid(row=0, column=2, padx=5, pady=5)
    
    # Platform Selection
    tk.Label(top_frame, text="Platform:").grid(row=0, column=3, padx=5, pady=5)
    app.platform_combobox = ttk.Combobox(top_frame, values=["Windows", "Linux", "Mac"])
    app.platform_combobox.grid(row=0, column=4, padx=5, pady=5)
    app.platform_combobox.bind("<<ComboboxSelected>>", app.update_command_options)
    
    # Command Selection
    tk.Label(top_frame, text="Command:").grid(row=0, column=5, padx=5, pady=5)
    app.command_combobox = ttk.Combobox(top_frame)
    app.command_combobox.grid(row=0, column=6, padx=5, pady=5)
    app.command_combobox.bind("<<ComboboxSelected>>", app.update_manual_entry)
    
    # Manual Command Entry
    tk.Label(top_frame, text="Manual:").grid(row=1, column=0, padx=5, pady=5)
    app.manual_entry = tk.Entry(top_frame, width=80)
    app.manual_entry.grid(row=1, column=1, columnspan=5, padx=5, pady=5)
    
    # Scan Button
    app.scan_button = tk.Button(top_frame, text="Scan", command=app.scan_file)
    app.scan_button.grid(row=0, column=7, rowspan=2, padx=5, pady=5, ipadx=10, ipady=5)
    
    # Command Parameter Selection Frame
    param_frame = tk.Frame(app)
    param_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
    
    tk.Label(param_frame, text="Command Parameter", font=('Helvetica', 10, 'bold')).pack(anchor=tk.W)
    
    # Initialize command parameter checkboxes
    app.param_vars = {
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
    
    for param, var in app.param_vars.items():
        tk.Checkbutton(param_frame, text=param, variable=var).pack(anchor=tk.W)
    
    # Main Display Frame
    display_frame = tk.Frame(app)
    display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Progress Bar
    app.progress_bar = ttk.Progressbar(display_frame, mode='indeterminate')
    app.progress_bar.pack(fill=tk.X, pady=5)
    
    # Results Table
    columns = ["PID", "PPID", "ImageFileName", "Offset(V)", "Threads", "SessionId", "Wow64", "CreateTime", "ExitTime", "File output"]
    app.tree = ttk.Treeview(display_frame, columns=columns, show='headings')
    for col in columns:
        app.tree.heading(col, text=col)
        app.tree.column(col, anchor=tk.W, stretch=tk.NO, width=100)
    
    app.tree.pack(fill=tk.BOTH, expand=True)
    
    # Status Bar
    app.status = tk.StringVar()
    app.status.set("Status: Ready")
    tk.Label(app, textvariable=app.status, bd=1, relief=tk.SUNKEN, anchor=tk.W).pack(side=tk.BOTTOM, fill=tk.X)

def browse_file(app):
    """
    Open a file dialog to browse and select a file.
    """
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Mem files", "*.mem"), ("Raw files", "*.raw")])
    if file_path:
        app.file_entry.delete(0, tk.END)
        app.file_entry.insert(0, file_path)

def scan_file(app):
    """
    Send a scan request to the backend API with the selected file and command.
    """
    file_path = app.file_entry.get()
    platform = app.platform_combobox.get().lower()
    command = app.command_combobox.get()
    
    # Ensure all fields are filled
    if not file_path or not platform or not command:
        app.status.set("Status: Please fill all the fields")
        return
    
    # Prepare JSON data for the request
    json_data = {
        "FilePath": file_path,
        "Command": command
    }
    
    app.progress_bar.start()
    app.status.set("Status: Scanning...")
    
    try:
        # Send the POST request to the backend API
        req = requests.post("http://localhost:6000/api/scan", json=json_data)
        app.progress_bar.stop()
        if req.status_code == 200:
            data = req.json()
            app.update_table(data['output'])
            app.status.set("Status: Scan completed")
        else:
            app.status.set(f"Status: Failed to fetch data - {req.status_code}")
    except requests.exceptions.RequestException as e:
        app.progress_bar.stop()
        app.status.set(f"Status: Error - {e}")

def update_command_options(app, event):
    """
    Update the available command options based on the selected platform.
    """
    platform = app.platform_combobox.get().lower()
    commands = {
        "windows": ["windows.pslist", "windows.info", "windows.psscan", "windows.pstree", "windows.dumpfiles", "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", "windows.netstat", "windows.registry.printkey", "windows.filescan"],
        "linux": ["linux.pslist", "linux.info", "linux.psscan", "linux.pstree", "linux.dumpfiles", "linux.memmap", "linux.handles", "linux.dlllist", "linux.cmdline", "linux.netscan", "linux.netstat", "linux.registry.printkey", "linux.filescan"],
        "mac": ["mac.pslist", "mac.info", "mac.psscan", "mac.pstree", "mac.dumpfiles", "mac.memmap", "mac.handles", "mac.dlllist", "mac.cmdline", "mac.netscan", "mac.netstat", "mac.registry.printkey", "mac.filescan"]
    }
    
    app.command_combobox['values'] = commands.get(platform, [])
    app.command_combobox.set('')
    app.manual_entry.delete(0, tk.END)

def update_manual_entry(app, event):
    """
    Update the manual command entry field based on the selected command.
    """
    command = app.command_combobox.get()
    file_path = app.file_entry.get() or "<file_path>"
    platform = app.platform_combobox.get().lower() or "<platform>"
    
    syntax = f"python vol.py -f {file_path} {command}"
    if command in ['windows.dumpfiles', 'windows.memmap', 'windows.handles', 'windows.dlllist', 'linux.dumpfiles', 'linux.memmap', 'linux.handles', 'linux.dlllist', 'mac.dumpfiles', 'mac.memmap', 'mac.handles', 'mac.dlllist']:
        syntax += " --pid <PID>"
    elif command in ['windows.vadyarascan', 'linux.vadyarascan', 'mac.vadyarascan']:
        syntax += " --yara-rules <rules>"
    
    app.manual_entry.delete(0, tk.END)
    app.manual_entry.insert(0, syntax)

def update_table(app, output):
    """
    Update the results table with the output from the scan command.
    """
    for i in app.tree.get_children():
        app.tree.delete(i)
    
    lines = output.strip().split("\n")
    for line in lines[1:]:  # Skip the header line
        app.tree.insert("", tk.END, values=line.split())
