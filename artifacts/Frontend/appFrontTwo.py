import tkinter as tk
import requests

jsonDATA = {
    "FilePath": "/Users/stefanspasenic/PycharmProjects/SmidiProject/artifacts/DumpFiles/20210430-Win10Home-20H2-64bit-memdump.mem",
    "OS": "windows",
    "Command": "psscan"
}


def scan_file():
    req = requests.post("http://localhost:6000/api/scan", json=jsonDATA)

    print(req)

    if req.status_code == 200:
        data = req.json()
        print(data)
        output_text = f"FilePath: {data['output']}\nError: {data['error']}"
        text_widget.delete(1.0, tk.END)  # Clear the text widget
        text_widget.insert(tk.END, output_text)  # Insert the new text


root = tk.Tk()
root.title("Tkinter and Flask Communication")

# Create a Text widget to display the data
text_widget = tk.Text(root, wrap='word', width=100, height=20)
text_widget.pack(pady=20)

# Create a button to fetch data
button = tk.Button(root, text="Fetch Data", command=scan_file)
button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()

root = tk.Tk()
root.title("Tkinter and Flask Communication")

# Create a label to display the data
label = tk.Label(root, text="Click the button to fetch data from Flask")
label.pack(pady=20)

# Create a button to fetch data
button = tk.Button(root, text="Fetch Data", command=scan_file)
button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
