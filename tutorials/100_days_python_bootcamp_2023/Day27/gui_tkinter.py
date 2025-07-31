from tkinter import Button, Entry, Label, Tk

window = Tk()
window.minsize(width=500, height=300)
window.title("My first GUI")

my_label = Label(window, text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    my_label.configure(text=input.get())


btn = Button(window, text="Click me!", command=button_clicked)
btn.pack()

input = Entry(window)
input.pack()

window.mainloop()
