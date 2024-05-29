import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Artifacts")

# Create a label
label = tk.Label(root, text="File:")
label.place(x=10, y=10)  # Adjust the coordinates as needed

# Create an entry field
file_entry = tk.Entry(root, width=50)
file_entry.insert(0, "IE10WN7-2022114-202804.raw")
file_entry.place(x=60, y=10)  # Adjust the coordinates as needed

# Start the GUI loop
root.mainloop()
