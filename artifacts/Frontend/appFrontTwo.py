import tkinter as tk
import requests

jsonDATA = {
    "FilePath": "C:/Users/evenj/OneDrive/Skrivebord/memdump-001.mem",
    "Command": "windows.pslist",
    "OS": "windows"
}

def scan_file():
    try:
        req = requests.post("http://localhost:6000/api/scan", json=jsonDATA)
        if req.status_code == 200:
            data = req.json()
            output_text = f"Output: {data['output']}\nError: {data['error']}"
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, output_text)
        else:
            text_widget.insert(tk.END, "Failed to fetch data")
    except requests.exceptions.RequestException as e:
        text_widget.insert(tk.END, f"Error: {e}")

root = tk.Tk()
root.title("Tkinter and Flask Communication")

text_widget = tk.Text(root, wrap='word', width=100, height=20)
text_widget.pack(pady=20)

button = tk.Button(root, text="Fetch Data", command=scan_file)
button.pack(pady=20)

root.mainloop()
