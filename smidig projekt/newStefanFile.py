import tkinter as tk
from tkinter import ttk
class SearchableCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._completion_list = []
        self._hits = []
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self.bind('<Button-1>', self.show_all_options)
        self.bind('<FocusIn>', self.on_focus_in)

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list)
        self['values'] = self._completion_list

    def autocomplete(self):
        search_term = self.get().lower()
        _hits = self.filter_hits(search_term)

        if _hits != self._hits:
            self._hits = _hits

        if _hits:
            self['values'] = _hits
            self.event_generate('<Down>')  # Open the dropdown

    def filter_hits(self, search_term):
        hits = [item for item in self._completion_list if search_term in item.lower()]
        return hits

    def handle_keyrelease(self, event):
        if event.keysym in ('Left', 'Right', 'Up', 'Down', 'BackSpace', 'Delete'):
            return
        self.position = len(self.get())
        self.autocomplete()
        self.icursor(self.position)  # Maintain the cursor position
        self.focus()  # Keep focus on the combobox

    def show_all_options(self, event=None):
        self['values'] = self._completion_list
        self.event_generate('<Down>')
        self.focus()

    def on_focus_in(self, event):
        self.icursor(self.position)

class StyledDropdown:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected_option = tk.StringVar(value="")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Scan:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=(0, 10), sticky=tk.W)

        self.combobox = SearchableCombobox(self.frame, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.show_selected_button = ttk.Button(self.frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    def show_selected(self):
        print("Selected item:", self.selected_option.get())

root = tk.Tk()
root.title("Searchable Dropdown Menu")
root.geometry("400x400")  # Set the size of the window

# List of options
options = [
    "windows.pslist", "windows.psscan", "windows.pstree", "windows.cmdline",
    "windows.services", "windows.registry", "windows.filescan", "windows.malware",
    "windows.network", "windows.memory", "windows.disk", "windows.eventlog",
    "windows.prefetch", "windows.timeline", "windows.locks", "windows.hooks",
    "windows.sysinfo", "windows.drivers", "windows.pipes", "windows.sockets"
]
sorted_options = sorted(options)
dropdown = StyledDropdown(root, sorted_options)

root.mainloop()

class KeyTracker:
    key = ''
    last_press_time = 0
    last_release_time = 0

    def track(self, key):
        self.key = key

    def is_pressed(self):
        return time.time() - self.last_press_time < .1

    def report_key_press(self, event):
        if event.keysym == self.key:
            if not self.is_pressed():
                on_key_press(event)
            self.last_press_time = time.time()

    def report_key_release(self, event):
        if event.keysym == self.key:
            timer = threading.Timer(.1, self.report_key_release_callback, args=[event])
            timer.start()

    def report_key_release_callback(self, event):
        if not self.is_pressed():
            on_key_release(event)
        self.last_release_time = time.time()