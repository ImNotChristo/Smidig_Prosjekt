import tkinter as tk
from tkinter import filedialog

# Opprette hovedvinduet 
root = tk.Tk()
root.title("Artifacts")

def open_file_dialog():
    # Åpne filvalgboksen og tillat brukeren å velge en fil
    filename = filedialog.askopenfilename(title="Velg en fil")

    # Oppdater tekstfeltet med den valgte filens sti
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)


# Opprette en etikett
label = tk.Label(root, text="File:")  # Tittelen som sier "File"
label.pack(side=tk.LEFT, padx=10, pady=10)  # Plasserer etiketten i vinduet med noe padding

# Opprette et tekstfelt
file_entry = tk.Entry(root, width=50)  # Tekstfeltet der filnavnet vanligvis vil vises
#file_entry.insert(0, "IE10WN7-2022114-202804.raw")  # Setter inn en eksempeltekst - kan fjernes
file_entry.pack(side=tk.LEFT, padx=10, pady=10)  # Plasserer tekstfeltet i vinduet med noe padding

# Knapp for å åpne filvalgboksen, fil pathen følger med når man velger en fil
button = tk.Button(root, text="Select Image File", command=open_file_dialog)
button.pack(side=tk.LEFT, padx=10, pady=10)

# Starte GUI-loop
root.mainloop() 