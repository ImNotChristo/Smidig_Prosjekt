import tkinter as tk

# Opprette hovedvinduet
root = tk.Tk()
root.title("Artifacts")

# Opprette en etikett
label = tk.Label(root, text="File:")  # Tittelen som sier "File"
label.pack(side=tk.LEFT, padx=10, pady=10)  # Plasserer etiketten i vinduet med noe padding

# Opprette et tekstfelt
file_entry = tk.Entry(root, width=50)  # Tekstfeltet der filnavnet vanligvis vil vises
file_entry.insert(0, "IE10WN7-2022114-202804.raw")  # Setter inn en eksempeltekst - kan fjernes
file_entry.pack(side=tk.LEFT, padx=10, pady=10)  # Plasserer tekstfeltet i vinduet med noe padding

# Starte GUI-loop
root.mainloop()