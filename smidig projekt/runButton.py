from tkinter import *


class RunButton:
    def __init__(self, master):
        self.master = master
        self.btn = None
        self.create_button()

    def create_button(self):
        self.btn = Button(self.master, text='RUN', command=self.master.destroy)
        self.btn.place(x=50, y=20)


root = Tk()
root.geometry('300x300')

# instance of RunButton
run_button = RunButton(root)
root.mainloop()