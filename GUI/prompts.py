import tkinter as tk
# from tkinter import font


def prompt(root, p="prompt here, then press ENTER"):
    prompt_window = tk.Tk()
    prompt_window.title('Prompt for Input')
    greeting = tk.Label(prompt_window, text=p, width=50)
    greeting.pack()
    entry = tk.Entry(prompt_window, width=5) # , fg="yellow", bg="blue"
    entry.pack()

    existing_window_position = f"+{root.winfo_rootx() + 300}+{root.winfo_rooty() + 300}"
    prompt_window.geometry(existing_window_position)

    def on_change(event):
        user_input = event.widget.get()
        print(user_input, '=======')
        prompt_window.destroy()

    entry.bind("<Return>", lambda event: on_change(event))
