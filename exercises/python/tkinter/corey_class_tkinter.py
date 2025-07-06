import tkinter as tk

root = tk.Tk()
root.title("Iavor first GUI program")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


def add_to_list(_event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)


frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry.bind("<Return>", add_to_list)

button = tk.Button(frame, text="Add", command=add_to_list)
button.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()
