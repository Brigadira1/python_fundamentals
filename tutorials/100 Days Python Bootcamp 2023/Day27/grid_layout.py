import tkinter as tk

root = tk.Tk()
root.wm_title("Iavor's GUI")
root.wm_minsize(width=600, height=300)
root.configure(padx=20, pady=20)


def button_click(_event=None):
    print("I got clicked")
    new_text = entry.get()
    label.configure(text=new_text)
    entry.delete(0, tk.END)


frame = tk.Frame(root)
frame.grid(row=0, column=0)

label = tk.Label(frame, text="Label")
label.grid(row=0, column=0)

button1 = tk.Button(frame, text="Click me!", command=button_click)
button1.grid(row=1, column=1)

new_button = tk.Button(frame, text="Click me second time!", command=button_click)
new_button.grid(row=0, column=2)

entry = tk.Entry(frame)
entry.grid(row=2, column=3)

root.mainloop()
