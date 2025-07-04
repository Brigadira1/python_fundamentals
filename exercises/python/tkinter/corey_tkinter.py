import tkinter as tk

root = tk.Tk()
root.title("Iavor first GUI program")


def add_to_list(_event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)


frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry.bind("<Return>", add_to_list)

button = tk.Button(frame, text="Add", command=add_to_list)
button.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="ew")

root.mainloop()
