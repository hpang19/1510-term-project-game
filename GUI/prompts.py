import tkinter as tk
# from tkinter import font


class Prompts:
    def __init__(self, frame):
        self.frame = frame
        self.entry_value = tk.StringVar()
        self.greeting = None
        self.entry = None
        self.entry_changed = False

    def on_return(self, event):
        self.entry_changed = True

    def wait_for_change(self):
        if not self.entry_changed:
            self.frame.after(100, self.wait_for_change)
        else:
            self.greeting.pack_forget()
            self.entry.pack_forget()

    def prompt(self, message):
        self.greeting = tk.Label(self.frame, text=message, width=50)
        self.greeting.pack()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_value, width=5)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_return)
        self.wait_for_change()
        self.frame.mainloop()
        return self.entry_value.get()
